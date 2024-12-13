from typing import Optional

from pydantic import BaseModel, Field


class Workers_create(BaseModel):
    name: str = Field(..., max_length=50)
    email: str = Field(..., max_length=50)


class Workers_update(BaseModel):
    name: Optional[str] = Field(None, max_length=50)
    email: Optional[str] = Field(None, max_length=50)
