from src.unit_of_work import UnitOfWork

from src.schemas.api.directions import DirectionOutput

class DirectionService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
    
    async def get_directions(self):
        result = await self.uow.repositories.direction.find_all()
        return [DirectionOutput(id=obj.id, name=obj.name) for obj in result]