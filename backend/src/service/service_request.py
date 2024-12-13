from src.unit_of_work import UnitOfWork

from src.schemas.api.service_requests import ServiceRequestInput

class ServiceRequestService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
    
    async def add_request(self, payload: ServiceRequestInput) -> None:
        await self.uow.notification.send_email(
            receivers=[obj.email for obj in (await self.uow.repositories.worker.find_all())],
            title="У вас новая запись на услугу!",
            body=(
                f"Новая запись на услугу:   {(await self.uow.repositories.service.find_one(id=payload.service_id)).name}\n\n" +
                f"Имя фамилия:   {payload.first_name} {payload.last_name}\n" +
                f"Телефон:   {payload.phone}\n"
                f"Дополнительные контакты:   {payload.additional_contacts}\n"
            )
        )
        await self.uow.repositories.service_requests.add_one(**payload.model_dump())
        await self.uow.commit()