from typing import Optional

from pydantic import BaseModel, Field


class Directions_create(BaseModel):
    name: str = Field(..., max_length=50)
    description: str = Field("", max_length=500)


class Directions_update(BaseModel):
    name: Optional[str] = Field(None, max_length=50)
    description: Optional[str] = Field(None, max_length=500)
