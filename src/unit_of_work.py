from typing import Any

from src.adapters.database.session import async_session_maker
from src.adapters.database.repository_gateway import RepositoriesGateway
from src.adapters.filestorage import FilestorageGateway

_sentinel: Any = object()


class UnitOfWork:
    repositories = _sentinel

    def __init__(self):
        self.db_session_factory = async_session_maker

    async def __aenter__(self):
        self.db_session = self.db_session_factory()

        self.repositories = RepositoriesGateway(self.db_session)
        self.filestorage = FilestorageGateway()

    async def __aexit__(self, *args):
        await self.rollback()
        await self.db_session.close()

    async def commit(self):
        await self.db_session.commit()

    async def rollback(self):
        await self.db_session.rollback()
