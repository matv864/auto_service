from datetime import datetime

from sqlalchemy import TIMESTAMP, String, DECIMAL, ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from src.utils.time import utc_signed_now


class Base(AsyncAttrs, DeclarativeBase):
    """
    Base class that provides metadata and id with int4
    """

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)


class BaseWithTelemetryTimestamps(Base):
    __abstract__ = True
    changing_date: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), default=utc_signed_now, onupdate=utc_signed_now
    )


class Manager(Base):
    __tablename__ = "managers"

    first_name: Mapped[str] = mapped_column(String(50))
    second_name: Mapped[str] = mapped_column(String(50))

    phone: Mapped[str] = mapped_column(String(11), unique=True)
    password: Mapped[str] = mapped_column(String(60))

    def __str__(self):
        return f"{self.first_name} {self.second_name}"


class Channel(Base):
    __tablename__ = "channels"

    name: Mapped[str] = mapped_column(String(50), unique=True)

    posts: Mapped[list["Post"]] = relationship(
        back_populates="channel", lazy="selectin", cascade="all, delete-orphan"
    )

    def __str__(self):
        return f"{self.name}"


class Post(BaseWithTelemetryTimestamps):
    __tablename__ = "posts"

    channel_id: Mapped[int] = mapped_column(ForeignKey("channels.id"))
    channel: Mapped[Channel] = relationship(
        back_populates="posts",
        lazy="selectin",
    )

    title: Mapped[str] = mapped_column(String(100))
    text: Mapped[str] = mapped_column(String(500), default="")

    image: Mapped[str] = mapped_column(nullable=True)

    def __str__(self):
        return f"{self.title} - {self.text[:10]}"


class Service(Base):
    __tablename__ = "services"

    name: Mapped[str] = mapped_column(String(50), unique=True)

    description: Mapped[str] = mapped_column(String(500), default="")
    price: Mapped[str] = mapped_column(String(50))

    service_requests: Mapped[list["ServiceRequest"]] = relationship(
        back_populates="service", lazy="selectin", cascade="all, delete-orphan"
    )

    def __str__(self):
        return f"{self.name}   {self.price}"
    

class ServiceRequest(BaseWithTelemetryTimestamps):
    __tablename__ = "service_requests"

    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))

    phone: Mapped[str] = mapped_column(String(20))
    additional_contacts: Mapped[str] = mapped_column(String(100), default="")

    service_id: Mapped[int] = mapped_column(ForeignKey("services.id"))
    service: Mapped[Service] = relationship(back_populates="service_requests", lazy="selectin")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Direction(Base):
    __tablename__ = "directions"

    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(500), default="")

    student_requests: Mapped[list["StudentRequest"]] = relationship(
        back_populates="direction", lazy="selectin", cascade="all, delete-orphan"
    )

    def __str__(self):
        return f"{self.name}"


class StudentRequest(BaseWithTelemetryTimestamps):
    __tablename__ = "student_requests"

    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    location: Mapped[str] = mapped_column(String(200))
    phone: Mapped[str] = mapped_column(String(20))
    additional_contacts: Mapped[str] = mapped_column(String(100), default="")
    

    direction_id: Mapped[int] = mapped_column(ForeignKey("directions.id"))
    direction: Mapped[Direction] = relationship(back_populates="student_requests", lazy="selectin")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Gallery(BaseWithTelemetryTimestamps):
    __tablename__ = "gallery"

    name: Mapped[str] = mapped_column(String(50), default="")
    image: Mapped[str]

    def __str__(self):
        return f"{self.name}"
    

class Worker(Base):
    __tablename__ = "workers"

    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))

    def __str__(self):
        return f"{self.name} {self.email}"