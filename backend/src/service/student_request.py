from src.unit_of_work import UnitOfWork

from src.schemas.api.student_requests import StudentRequestInput

class StudentRequestService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
    
    async def add_request(self, payload: StudentRequestInput) -> None:
        await self.uow.notification.send_email(
            receivers=[obj.email for obj in (await self.uow.repositories.worker.find_all())],
            title="У вас новая запись на обучение!",
            body=(
                "Новая запись на обучение по направлению:   " +
                f"{(await self.uow.repositories.direction.find_one(id=payload.direction_id)).name}\n\n" +
                f"Имя фамилия:   {payload.first_name} {payload.last_name}\n" +
                f"Локация:   {payload.location}\n" +
                f"Телефон:   {payload.phone}\n"
                f"Дополнительные контакты:   {payload.additional_contacts}\n"
            )
        )
        await self.uow.repositories.student_request.add_one(**payload.model_dump())
        await self.uow.commit()