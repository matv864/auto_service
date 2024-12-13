from fastadmin import WidgetType, register

from src.adapters.database.models import Service
from src.adapters.database.repositories import ServiceRepository
from src.adapters.database.session import async_session_maker
from src.admin.user_custom_fastadmin import CustomModelAdmin

from src.schemas.admin.services import Services_create, Services_update


@register(Service, sqlalchemy_sessionmaker=async_session_maker)
class ServiceAdmin(CustomModelAdmin):
    Service.__name__ = "Услуги"

    schema_create = Services_create
    schema_update = Services_update

    model_repository = ServiceRepository

    list_display = ("name", "price", "description")
    list_display_links = ("name",)
    list_filter = ("name",)

    search_fields = ("name",)

    fieldsets = ((None, {"fields": ("name", "description", "price")},),)
    formfield_overrides = {
        "name": (WidgetType.Input, {"required": True}),
        "decription": (WidgetType.TextArea, {"required": False}),
        "price": (WidgetType.InputNumber, {"required": True})
    }
