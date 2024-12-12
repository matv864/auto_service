from src.unit_of_work import UnitOfWork


class PostService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
    
    async def get_posts(self, channel_id: int):
        return await self.uow.repositories.post.find_filtered(channel_id=channel_id)