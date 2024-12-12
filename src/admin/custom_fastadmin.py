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
        sessionmaker = self.get_sessionmaker()
        async with sessionmaker() as session:
            obj = await session.get(self.model_cls, id)
            return obj

    async def orm_delete_obj(self, id: int) -> None:
        """This method is used to delete orm/db model object.

        :params id: an id of object.
        :return: None.
        """
        sessionmaker = self.get_sessionmaker()
        async with sessionmaker() as session:
            obj = await session.get(self.model_cls, id)
            await session.delete(obj)
            await session.commit()
