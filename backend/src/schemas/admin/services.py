from typing import Optional
from decimal import Decimal

from pydantic import BaseModel, Field


class Services_create(BaseModel):
    name: str = Field(..., max_length=50)
    description: str = Field("", max_length=300)
    price: Decimal = Field(..., decimal_places=2, lt=10**9, gt=0)


class Services_update(BaseModel):
    name: Optional[str] = Field(None, max_length=50)
    description: str = Field("", max_length=300)
    price: Optional[Decimal] = Field(None, decimal_places=2, lt=10**9, gt=0)
