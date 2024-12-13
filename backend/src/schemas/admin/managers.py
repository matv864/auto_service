from typing import Optional

from pydantic import BaseModel, Field


class Managers_create(BaseModel):
    first_name: str = Field(..., max_length=50)
    second_name: str = Field(..., max_length=50)

    phone: str = Field(..., max_length=11)
    password: str


class Managers_update(BaseModel):
    first_name: Optional[str] = Field(None, max_length=50)
    second_name: Optional[str] = Field(None, max_length=50)

    phone: Optional[str] = Field(None, max_length=11)
    password: Optional[str] = None
