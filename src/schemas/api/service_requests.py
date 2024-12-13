from pydantic import BaseModel, ConfigDict, Field


class ServiceRequestInput(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    first_name: str = Field(..., max_length=30)
    last_name: str = Field(..., max_length=30)
    additional_contacts: str = Field(..., max_length=100)
    phone: str = Field(pattern=r"^7\d{10,19}$")

    service_id: int


class ServiceRequestOutput(BaseModel):
    pass