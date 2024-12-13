from fastadmin import WidgetType, register

from src.adapters.database.models import Manager
from src.adapters.database.repositories import ManagerRepository
from src.adapters.database.session import async_session_maker
from src.admin.user_custom_fastadmin import UserCustomModelAdmin

from src.schemas.admin.managers import Managers_create, Managers_update


@register(Manager, sqlalchemy_sessionmaker=async_session_maker)
class ManagerAdmin(UserCustomModelAdmin):
    Manager.__name__ = "Менеджеры"

    schema_create = Managers_create
    schema_update = Managers_update

    model_repository = ManagerRepository

    list_display = ("phone", "first_name", "second_name")
    list_display_links = ("phone",)
    list_filter = ("phone", "first_name", "second_name")

    search_fields = (
        "first_name",
        "second_name",
        "phone",
    )

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "first_name",
                    "second_name",
                    "phone",
                    "password",
                )
            },
        ),
    )
    formfield_overrides = {  # noqa: RUF012
        "first_name": (WidgetType.Input, {"required": True}),
        "second_name": (WidgetType.Input, {"required": True}),
        "phone": (WidgetType.PhoneInput, {"required": True}),
        "password": (WidgetType.PasswordInput, {"passwordModalForm": True}),
    }
