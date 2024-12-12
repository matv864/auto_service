from abc import abstractmethod
from typing import Any, Protocol

from bcrypt import checkpw, gensalt, hashpw
from sqlalchemy import func, insert, select, update
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.base import ExecutableOption

from src.utils.exceptions import ForeignKeyError, ResultNotFound, WrongCredentials

_sentinel: Any = object()


class AbstractRepository(Protocol):
    @abstractmethod
    async def add_one(self, **data):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = _sentinel

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, **data):
        stmt = insert(self.model).values(**data).returning(self.model)
        try:
            res = await self.session.execute(stmt)
            return res.scalar_one()
        except IntegrityError:
            raise ForeignKeyError

    async def edit_one(self, id: int, **data):
        stmt = update(self.model).values(**data).filter_by(id=id).returning(self.model)
        try:
            res = await self.session.execute(stmt)
            return res.unique().scalar_one()
        except NoResultFound:
            raise ResultNotFound
        except IntegrityError:
            raise ForeignKeyError

    async def find_all(self):
        stmt = select(self.model).options(*self.get_select_options())
        res = await self.session.execute(stmt)
        return res.unique().scalars().fetchall()

    async def find_filtered(self, **filter_by):
        stmt = (
            select(self.model)
            .options(*self.get_select_options())
            .filter_by(**filter_by)
        )
        res = await self.session.execute(stmt)
        return res.unique().scalars().fetchall()

    async def find_filtered_and_paginated(self, page: int, limit: int, **filter_by):
        stmt = (
            select(self.model)
            .options(*self.get_select_options())
            .filter_by(**filter_by)
            .offset((page - 1) * limit)
            .limit(limit)
        )

        res = await self.session.execute(stmt)
        return res.unique().scalars().fetchall()

    async def find_one(self, **filter_by):
        stmt = (
            select(self.model)
            .options(*self.get_select_options())
            .filter_by(**filter_by)
        )
        res = await self.session.execute(stmt)
        try:
            return res.scalar_one()
        except NoResultFound:
            raise ResultNotFound

    async def count_filtered(self, **filter_by):
        stmt = (
            select(func.count())
            .select_from(self.model)
            .options(*self.get_select_options())
            .filter_by(**filter_by)
        )
        res = await self.session.execute(stmt)
        return res.unique().scalar_one()

    async def find_filtered_in(self, column_name: str, values: list):
        stmt = (
            select(self.model)
            .options(*self.get_select_options())
            .filter(getattr(self.model, column_name).in_(values))
        )
        res = await self.session.execute(stmt)
        return res.unique().scalars().fetchall()

    async def delete_one(self, id: int) -> None:
        await self.session.delete((await self.find_one(id=id)))

    def get_select_options(self) -> list[ExecutableOption]:
        return []


class SQLALchemyUserRepository(SQLAlchemyRepository):
    async def authenticate(self, phone: str, password: str):
        try:
            user = await self.find_one(phone=phone)
        except ResultNotFound:
            raise WrongCredentials

        if not checkpw(password.encode(), user.password.encode()):
            raise WrongCredentials

        return user

    async def register(self, **data):
        data["password"] = hashpw(data["password"].encode(), gensalt()).decode()
        return await self.add_one(**data)

    async def change_password(self, id: int, password: str):
        password = hashpw(password.encode(), gensalt()).decode()
        return await self.edit_one(id, password=password)
