from pydantic import BaseModel, ConfigDict


class ChannelInfo(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str


class ChannelOutput(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    items: list[ChannelInfo]
