from src.unit_of_work import UnitOfWork

from src.schemas.api.services import ServiceOutput


class ServiceService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
    
    async def get_services(self):
        result = await self.uow.repositories.service.find_all()
        return [ServiceOutput(id=obj.id, name=obj.name, description=obj.description, price=obj.price) for obj in result]