from typing import Optional
from decimal import Decimal

from pydantic import BaseModel, Field


class Services_create(BaseModel):
    name: str = Field(..., max_length=50)
    description: str = Field("", max_length=300)
    price: str = Field(..., max_length=50)


class Services_update(BaseModel):
    name: Optional[str] = Field(None, max_length=50)
    description: str = Field("", max_length=300)
    price: Optional[str] = Field(None, max_length=50)
