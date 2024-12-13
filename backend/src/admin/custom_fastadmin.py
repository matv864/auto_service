import base64
import binascii
from io import BytesIO
from typing import Any

from fastadmin import SqlAlchemyModelAdmin

from src.unit_of_work import UnitOfWork
from src.utils.repository import SQLAlchemyRepository

_sentinel: Any = object()


class CustomModelAdmin(SqlAlchemyModelAdmin):
    schema_create = _sentinel
    schema_update = _sentinel

    uow = UnitOfWork()
    model_repository = _sentinel

    async def save_model(self, id: int | None, payload: dict) -> dict | None:
        """This method is used to save orm/db model object.

        :params id: an id of object.
        :params payload: a payload from request.
        :return: A saved object or None.
        """
        fields = self.get_model_fields_with_widget_types(
            with_m2m=False, with_upload=False
        )
        upload_fields = self.get_model_fields_with_widget_types(with_upload=True)

        fields_payload = {
            field.column_name: self.deserialize_value(field, payload[field.name])
            for field in fields
            if field.name in payload
        }
        fields_payload["id"] = id

        for upload_field in upload_fields:
            if upload_field.name in payload and is_valid_base64(
                payload[upload_field.name]
            ):
                await self.orm_save_upload_field(
                    fields_payload, upload_field.name, payload[upload_field.name]
                )

        if upload_fields and fields_payload.get(upload_fields[0].name):
            obj = None
            upload_field_name = upload_fields[0].name
            upload_field_links = fields_payload[upload_field_name]

            for upload_field_link in upload_field_links:
                fields_payload[upload_field_name] = upload_field_link
                obj = await self.orm_save_obj(id, fields_payload)
        else:
            obj = await self.orm_save_obj(id, fields_payload)

        if not obj:
            return None

        return await self.serialize_obj(obj)

    async def orm_save_obj(self, id: int | None, payload: dict) -> Any:
        async with self.uow:
            repo: SQLAlchemyRepository = self.model_repository(self.uow.db_session)
            if id:
                if self.schema_update:
                    pydantic_obj = self.schema_update(**payload)
                    payload = pydantic_obj.model_dump(exclude_none=True)
                res = await repo.edit_one(id, **payload)
            else:
                if self.schema_create:
                    pydantic_obj = self.schema_create(**payload)
                    payload = pydantic_obj.model_dump(exclude_none=True)
                res = await repo.add_one(**payload)
            await self.uow.commit()
        return res

    async def orm_get_obj(self, id: int) -> Any | None:
        """This method is used to get orm/db model object.

        :params id: an id of object.
        :return: An object.
        """
        upload_fields = self.get_model_fields_with_widget_types(with_upload=True)
        sessionmaker = self.get_sessionmaker()
        async with sessionmaker() as session:
            obj = await session.get(self.model_cls, id)
            if upload_fields:
                async with self.uow:
                    upload_field_name = upload_fields[0].column_name
                    link = self.uow.filestorage.get_file_url(
                        getattr(obj, upload_field_name)
                    )
                    setattr(obj, upload_field_name, link)
            return obj

    async def orm_delete_obj(self, id: int) -> None:
        """This method is used to delete orm/db model object.

        :params id: an id of object.
        :return: None.
        """
        upload_fields = self.get_model_fields_with_widget_types(with_upload=True)
        sessionmaker = self.get_sessionmaker()
        async with sessionmaker() as session:
            obj = await session.get(self.model_cls, id)
            if upload_fields:
                async with self.uow:
                    upload_field_name = upload_fields[0].column_name
                    self.uow.filestorage.delete_file(
                        getattr(obj, upload_field_name)
                    )
            await session.delete(obj)
            await session.commit()

    async def orm_save_upload_field(
        self, new_record: dict, field_name: str, data: str
    ) -> None:
        upload_fields = self.get_model_fields_with_widget_types(with_upload=True)

        # delete old obj
        if new_record.get("id"):
            sessionmaker = self.get_sessionmaker()
            async with sessionmaker() as session:
                obj = await session.get(self.model_cls, new_record.get("id"))
                filename = getattr(obj, upload_fields[0].name)
                async with self.uow:
                    self.uow.filestorage.delete_file(filename)

        # data:image/jpeg;base64...
        metadata, file_base64 = data.split(";base64,")
        mimetype = metadata.replace("data:", "")
        file = BytesIO(base64.b64decode(file_base64))
        async with self.uow:
            new_filename: str = self.uow.filestorage.upload_file(file, mimetype)
        new_record[field_name] = [
            new_filename,
        ]


def is_valid_base64(value: str) -> bool:
    try:
        value = value.split(";base64,")[1]
        base64.decodebytes(value.encode("ascii"))
        return True
    except binascii.Error:
        return False
    except IndexError:
        return False
