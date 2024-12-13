from pydantic import BaseModel, ConfigDict


class ServiceOutput(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    description: str
    price: float
