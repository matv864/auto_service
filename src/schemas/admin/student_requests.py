from typing import Optional

from pydantic import BaseModel, Field



class Student_requests_create(BaseModel):
    fisrt_name: str = Field(..., max_length=30)
    last_name: str = Field(..., max_length=30)
    phone: str = Field(..., max_length=11)

class Student_requests_update(BaseModel):
    fisrt_name: Optional[str] = Field(None, max_length=30)
    last_name: Optional[str] = Field(None, max_length=30)
    phone: Optional[str] = Field(None, max_length=11)