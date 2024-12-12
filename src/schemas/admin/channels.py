from typing import Optional

from pydantic import BaseModel, Field


class Channels_create(BaseModel):
    name: str = Field(..., max_length=50)


class Channels_update(BaseModel):
    name: Optional[str] = Field(None, max_length=50)
