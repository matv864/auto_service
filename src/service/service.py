from src.unit_of_work import UnitOfWork


class ServiceService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
    
    async def get_services(self):
        return await self.uow.repositories.service.find_all()