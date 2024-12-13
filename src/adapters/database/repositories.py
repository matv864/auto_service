from src.utils.repository import SQLAlchemyRepository, SQLALchemyUserRepository

from .models import (
    Manager,
    Channel,
    Post,
    Service,
    Direction,
    StudentRequest
)


class ManagerRepository(SQLALchemyUserRepository):
    model = Manager


class ChannelRepository(SQLAlchemyRepository):
    model = Channel


class PostRepository(SQLAlchemyRepository):
    model = Post


class ServiceRepository(SQLAlchemyRepository):
    model = Service


class DirectionRepository(SQLAlchemyRepository):
    model = Direction


class StudentRequestRepository(SQLAlchemyRepository):
    model = StudentRequest

