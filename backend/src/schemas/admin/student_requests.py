from typing import Optional

from pydantic import BaseModel, Field



class Student_requests_create(BaseModel):
    first_name: str = Field(..., max_length=30)
    last_name: str = Field(..., max_length=30)
    location: str = Field(..., max_length=200)
    additional_contacts: str = Field("", max_length=100)
    phone: str = Field(..., max_length=20)

    direction_id: int

class Student_requests_update(BaseModel):
    first_name: Optional[str] = Field(None, max_length=30)
    last_name: Optional[str] = Field(None, max_length=30)
    location: Optional[str] = Field(None, max_length=200)
    additional_contacts: Optional[str] = Field(None, max_length=100)
    phone: Optional[str] = Field(None, max_length=20)

    direction_id: Optional[int] = None
