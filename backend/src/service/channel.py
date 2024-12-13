from src.unit_of_work import UnitOfWork

from src.schemas.api.channels import ChannelOutput

class ChannelService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
    
    async def get_channels(self):
        result = await self.uow.repositories.channel.find_all()
        return [ChannelOutput(id=obj.id, name=obj.name) for obj in result]