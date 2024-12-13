from fastadmin import WidgetType, register

from src.adapters.database.models import Worker
from src.adapters.database.repositories import WorkerRepository
from src.adapters.database.session import async_session_maker
from src.admin.user_custom_fastadmin import CustomModelAdmin

from src.schemas.admin.workers import Workers_create, Workers_update


@register(Worker, sqlalchemy_sessionmaker=async_session_maker)
class ServiceAdmin(CustomModelAdmin):
    Worker.__name__ = "Сотрудники"

    schema_create = Workers_create
    schema_update = Workers_update

    model_repository = WorkerRepository

    list_display = ("name", "email")
    list_display_links = ("name",)
    list_filter = ("name", "email")

    search_fields = ("name", "email")

    fieldsets = ((None, {"fields": ("name", "email")},),)
    formfield_overrides = {
        "name": (WidgetType.Input, {"required": True}),
        "email": (WidgetType.EmailInput, {"required": True})
    }
