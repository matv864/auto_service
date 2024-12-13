from typing import Annotated

from fastapi import APIRouter, Depends

from src.service.channel import ChannelService
from src.service.post import PostService
from src.service.service import ServiceService
from src.service.service_request import ServiceRequestService
from src.service.direction import DirectionService
from src.service.student_request import StudentRequestService


from src.schemas.api.channels import ChannelOutput
from src.schemas.api.posts import PostOutput
from src.schemas.api.services import ServiceOutput
from src.schemas.api.service_requests import ServiceRequestInput, ServiceRequestOutput
from src.schemas.api.directions import DirectionOutput
from src.schemas.api.student_requests import StudentRequestInput, StudentRequestOutput

from src.unit_of_work import UnitOfWork

auto_service_router = APIRouter()


@auto_service_router.get("/channels", response_model=list[ChannelOutput])
async def get_channels(
    uow: Annotated[UnitOfWork, Depends(UnitOfWork)]
):
    async with uow:
        return await ChannelService(uow).get_channels()


@auto_service_router.get("/posts", response_model=list[PostOutput])
async def get_posts_from_channel(
    uow: Annotated[UnitOfWork, Depends(UnitOfWork)],
    channel_id: int
):
    async with uow:
        return await PostService(uow).get_posts(channel_id=channel_id)


@auto_service_router.get("/services", response_model=list[ServiceOutput])
async def get_services(
    uow: Annotated[UnitOfWork, Depends(UnitOfWork)]
):
    async with uow:
        return await ServiceService(uow).get_services()

@auto_service_router.post("/service-request", response_model=ServiceRequestOutput)
async def add_service_request(
    uow: Annotated[UnitOfWork, Depends(UnitOfWork)],
    payload: ServiceRequestInput
):
    async with uow:
        await ServiceRequestService(uow).add_request(payload)
    return dict()


@auto_service_router.get("/directions", response_model=list[DirectionOutput])
async def get_directions(
    uow: Annotated[UnitOfWork, Depends(UnitOfWork)]
):
    async with uow:
        return await DirectionService(uow).get_directions()

@auto_service_router.post("/student-request", response_model=StudentRequestOutput)
async def add_student_request(
    uow: Annotated[UnitOfWork, Depends(UnitOfWork)],
    payload: StudentRequestInput
):
    async with uow:
        await StudentRequestService(uow).add_request(payload)
    return dict()
