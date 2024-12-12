from fastadmin import WidgetType, register

from src.adapters.database.models import StudentRequest
from src.adapters.database.repositories import StudentRequestRepository
from src.adapters.database.session import async_session_maker
from src.admin.user_custom_fastadmin import CustomModelAdmin

from src.schemas.admin.student_requests import Student_requests_create, Student_requests_update


@register(StudentRequest, sqlalchemy_sessionmaker=async_session_maker)
class ServiceAdmin(CustomModelAdmin):
    StudentRequest.__name__ = "Заявки"

    schema_create = Student_requests_create
    schema_update = Student_requests_update

    model_repository = StudentRequestRepository

    list_display = ("fisrt_name", "last_name", "phone")
    list_display_links = ("fisrt_name", "last_name")
    list_filter = ("fisrt_name", "last_name")

    search_fields = ("fisrt_name", "last_name")

    fieldsets = ((None, {"fields": ("fisrt_name", "last_name", "phone")},),)
    formfield_overrides = {
        "fisrt_name": (WidgetType.Input, {"required": True}),
        "last_name": (WidgetType.Input, {"required": True}),
        "phone": (WidgetType.PhoneInput, {"required": True})
    }
