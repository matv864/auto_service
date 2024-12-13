from src.unit_of_work import UnitOfWork

from src.schemas.api.gallery import GalleryOutput


class GalleryService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
    
    async def get_gallery(self):
        result = await self.uow.repositories.gallery.find_all()
        return [
            GalleryOutput(
                name=obj.name,
                image=self.uow.filestorage.get_file_url(obj.image)
            ) for obj in result
        ]