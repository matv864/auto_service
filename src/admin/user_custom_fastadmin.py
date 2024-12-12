from typing import Any

from bcrypt import gensalt, hashpw

from src.utils.exceptions import WrongCredentials
from src.utils.repository import SQLALchemyUserRepository

from .custom_fastadmin import CustomModelAdmin


class UserCustomModelAdmin(CustomModelAdmin):
    async def authenticate(self, phone: str, password: str):
        async with self.uow:
            repo: SQLALchemyUserRepository = self.model_repository(self.uow.db_session)
            try:
                user = await repo.authenticate(phone, password)
                return user.id
            except WrongCredentials:
                return None
    
    async def change_password(self, id: int, password: str) -> None:
        async with self.uow:
            repo: SQLALchemyUserRepository = self.model_repository(self.uow.db_session)
            await repo.change_password(id, password)
            await self.uow.commit()

    async def orm_save_obj(self, id: int | None, payload: dict) -> Any:
        async with self.uow:
            repo: SQLALchemyUserRepository = self.model_repository(self.uow.db_session)
            if id:
                new_password = payload.pop("password")
                if self.schema_update:
                    pydantic_obj = self.schema_update(**payload)
                    if not (
                        await self.new_password_is_old_pasword(repo, id, new_password)
                    ):
                        pydantic_obj.password = hashpw(
                            new_password.encode(), gensalt()
                        ).decode()
                    payload = pydantic_obj.model_dump(exclude_none=True)
                    # special case when email is "" (pydantic model give None in that case, but exclude_none need to be true)
                    payload["email"] = payload.get("email", None)
                res = await repo.edit_one(id, **payload)

            else:
                if self.schema_create:
                    pydantic_obj = self.schema_create(**payload)
                    payload = pydantic_obj.model_dump(exclude_none=True)
                res = await repo.register(**payload)
            await self.uow.commit()
        return res

    async def new_password_is_old_pasword(
        self, repo: SQLALchemyUserRepository, id: int, new_password: str
    ) -> bool:
        user = await repo.find_one(id=id)
        return new_password.encode() == user.password.encode()
