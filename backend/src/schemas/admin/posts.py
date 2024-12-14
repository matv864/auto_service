from typing import Optional

from pydantic import BaseModel, Field


class Posts_create(BaseModel):
    channel_id: int
    title: str = Field(..., max_length=100)
    text: str = Field("", max_length=500)
    image: Optional[str] = None


class Posts_update(BaseModel):
    channel_id: Optional[int] = None
    title: Optional[str] = Field(None, max_length=100)
    text: Optional[str] = Field(None, max_length=500)
    image: Optional[str] = None
