from pydantic import BaseModel, ConfigDict, Field


class StudentRequestInput(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    first_name: str = Field(..., max_length=30)
    last_name: str = Field(..., max_length=30)
    phone: str = Field(pattern=r"^7\d{10}$")


class StudentRequestOutput(BaseModel):
    pass