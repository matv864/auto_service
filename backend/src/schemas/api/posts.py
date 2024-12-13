from pydantic import BaseModel, ConfigDict


class PostOutput(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    channel_id: int
    title: str
    text: str
    image: str