from src.utils.repository import SQLAlchemyRepository, SQLALchemyUserRepository

from .models import (
    Manager,
    Channel,
    Post,
    Service
)


class ManagerRepository(SQLALchemyUserRepository):
    model = Manager


class ChannelRepository(SQLAlchemyRepository):
    model = Channel


class PostRepository(SQLAlchemyRepository):
    model = Post


class ServiceRepository(SQLAlchemyRepository):
    model = Service

