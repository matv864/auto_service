from src.unit_of_work import UnitOfWork

from src.schemas.api.posts import PostOutput


class PostService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
    
    async def get_posts(self, channel_id: int):
        result = await self.uow.repositories.post.find_filtered(channel_id=channel_id)
        return [
            PostOutput(
                channel_id=obj.channel_id,
                title=obj.title,
                text=obj.text,
                image=self.uow.filestorage.get_file_url(obj.image)
            ) for obj in result
        ]