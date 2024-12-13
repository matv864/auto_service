from src.unit_of_work import UnitOfWork

from src.schemas.api.service_requests import ServiceRequestInput

class ServiceRequestService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
    
    async def add_request(self, payload: ServiceRequestInput) -> None:
        await self.uow.repositories.service_requests.add_one(**payload.model_dump())
        await self.uow.commit()