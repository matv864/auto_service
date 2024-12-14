from fastadmin import WidgetType, register

from src.adapters.database.models import Direction
from src.adapters.database.repositories import DirectionRepository
from src.adapters.database.session import async_session_maker
from src.admin.user_custom_fastadmin import CustomModelAdmin

from src.schemas.admin.directions import Directions_create, Directions_update


@register(Direction, sqlalchemy_sessionmaker=async_session_maker)
class ChannelAdmin(CustomModelAdmin):
    Direction.__name__ = "Направления"

    schema_create = Directions_create
    schema_update = Directions_update

    model_repository = DirectionRepository

    list_display = ("name", "description")
    list_display_links = ("name",)
    list_filter = ("name", "description")

    search_fields = ("name", "description")

    fieldsets = ((None, {"fields": ("name", "description")},),)
    formfield_overrides = {
        "name": (WidgetType.Input, {"required": True}),
        "description": (WidgetType.TextArea, {"required": False}),
    }
