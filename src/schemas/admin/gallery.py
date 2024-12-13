from typing import Optional

from pydantic import BaseModel, Field


class Gallery_create(BaseModel):
    name: str = Field("", max_length=50)
    image: str


class Gallery_update(BaseModel):
    name: str = Field("", max_length=50)
    image: Optional[str] = None
