from src.unit_of_work import UnitOfWork


class ChannelService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
    
    async def get_channels(self):
        return await self.uow.repositories.channel.find_all()