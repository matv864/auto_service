from pydantic import BaseModel, ConfigDict


class PostInfo(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    channel_id: int
    title: str
    text: str


class PostOutput(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    items: list[PostInfo]