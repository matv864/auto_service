from fastadmin import WidgetType, register

from src.adapters.database.models import Channel
from src.adapters.database.repositories import ChannelRepository
from src.adapters.database.session import async_session_maker
from src.admin.user_custom_fastadmin import CustomModelAdmin

from src.schemas.admin.channels import Channels_create, Channels_update


@register(Channel, sqlalchemy_sessionmaker=async_session_maker)
class ChannelAdmin(CustomModelAdmin):
    Channel.__name__ = "Каналы"

    schema_create = Channels_create
    schema_update = Channels_update

    model_repository = ChannelRepository

    list_display = ("name",)
    list_display_links = ("name",)
    list_filter = ("name",)

    search_fields = ("name",)

    fieldsets = ((None, {"fields": ("name",)},),)
    formfield_overrides = {"name": (WidgetType.Input, {"required": True}),}
