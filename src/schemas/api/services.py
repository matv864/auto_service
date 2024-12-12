from pydantic import BaseModel, ConfigDict


class ServiceInfo(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    description: str
    price: float


class ServiceOutput(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    items: list[ServiceInfo]
