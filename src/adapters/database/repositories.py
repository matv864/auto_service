from src.utils.repository import SQLAlchemyRepository, SQLALchemyUserRepository

from .models import (
    Manager,
    Channel,
    Post,
    Service,
    ServiceRequest,
    Direction,
    StudentRequest,
    Gallery
)


class ManagerRepository(SQLALchemyUserRepository):
    model = Manager


class ChannelRepository(SQLAlchemyRepository):
    model = Channel


class PostRepository(SQLAlchemyRepository):
    model = Post


class ServiceRepository(SQLAlchemyRepository):
    model = Service


class ServiceRequestRepository(SQLAlchemyRepository):
    model = ServiceRequest


class DirectionRepository(SQLAlchemyRepository):
    model = Direction


class StudentRequestRepository(SQLAlchemyRepository):
    model = StudentRequest


class GalleryRepository(SQLAlchemyRepository):
    model = Gallery
