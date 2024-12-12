from src.unit_of_work import UnitOfWork

from src.schemas.api.student_requests import StudentRequestInput

class StudentRequestService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
    
    async def add_request(self, payload: StudentRequestInput) -> None:
        await self.uow.repositories.student_request.add_one(**payload)
        await self.uow.commit()