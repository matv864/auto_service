from sqlalchemy.ext.asyncio import AsyncSession

from src.adapters.database.repositories import (
    ChannelRepository,
    PostRepository,
    ServiceRepository,
    DirectionRepository,
    StudentRequestRepository,
)


class RepositoriesGateway:
    def __init__(self, session: AsyncSession):
        self.channel = ChannelRepository(session)
        self.post = PostRepository(session)
        self.service = ServiceRepository(session)
        self.direction = DirectionRepository(session)
        self.student_request = StudentRequestRepository(session)
       