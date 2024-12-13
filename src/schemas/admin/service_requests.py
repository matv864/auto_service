from typing import Optional

from pydantic import BaseModel, Field



class Service_requests_create(BaseModel):
    first_name: str = Field(..., max_length=30)
    last_name: str = Field(..., max_length=30)
    additional_contacts: str = Field("", max_length=100)
    phone: str = Field(..., max_length=20)

    service_id: int

class Service_requests_update(BaseModel):
    first_name: Optional[str] = Field(None, max_length=30)
    last_name: Optional[str] = Field(None, max_length=30)
    additional_contacts: str = Field(None, max_length=100)
    phone: Optional[str] = Field(None, max_length=20)

    service_id: Optional[int] = None
