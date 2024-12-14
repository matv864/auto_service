from pydantic import BaseModel, ConfigDict


class ServiceOutput(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: str
    price: str
