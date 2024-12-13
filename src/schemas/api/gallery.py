from pydantic import BaseModel, Field


class GalleryOutput(BaseModel):
    name: str = Field("", max_length=50)
    image: str
