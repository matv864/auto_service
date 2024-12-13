from fastadmin import WidgetType, register

from src.adapters.database.models import StudentRequest
from src.adapters.database.repositories import StudentRequestRepository
from src.adapters.database.session import async_session_maker
from src.admin.user_custom_fastadmin import CustomModelAdmin

from src.schemas.admin.student_requests import Student_requests_create, Student_requests_update


@register(StudentRequest, sqlalchemy_sessionmaker=async_session_maker)
class ServiceAdmin(CustomModelAdmin):
    StudentRequest.__name__ = "Обучение Заявки"

    schema_create = Student_requests_create
    schema_update = Student_requests_update

    model_repository = StudentRequestRepository

    list_display = ("first_name", "last_name", "direction", "phone")
    list_display_links = ("first_name", "last_name")
    list_filter = ("first_name", "last_name")

    search_fields = ("first_name", "last_name")
    raw_id_fields =("direction_id", )

    fieldsets = ((None, {"fields": ("first_name", "last_name", "location", "additional_contacts", "phone", "direction")},),)
    formfield_overrides = {
        "first_name": (WidgetType.Input, {"required": True}),
        "last_name": (WidgetType.Input, {"required": True}),
        "location": (WidgetType.TextArea, {"required": True}),
        "additional_contacts": (WidgetType.TextArea, {"required": False}),
        "phone": (WidgetType.PhoneInput, {"required": True})
    }
