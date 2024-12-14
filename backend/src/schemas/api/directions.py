from pydantic import BaseModel, ConfigDict


class DirectionOutput(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: str
