from pydantic import BaseModel, ConfigDict, Field


class StudentRequestInput(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    first_name: str = Field(..., max_length=30)
    last_name: str = Field(..., max_length=30)
    location: str = Field(..., max_length=200)
    additional_contacts: str = Field(..., max_length=100)
    phone: str = Field(pattern=r"^7\d{10,19}$")

    direction_id: int


class StudentRequestOutput(BaseModel):
    pass