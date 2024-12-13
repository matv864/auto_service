from fastadmin import WidgetType, register

from src.adapters.database.models import ServiceRequest
from src.adapters.database.repositories import ServiceRequestRepository
from src.adapters.database.session import async_session_maker
from src.admin.user_custom_fastadmin import CustomModelAdmin

from src.schemas.admin.service_requests import Service_requests_create, Service_requests_update


@register(ServiceRequest, sqlalchemy_sessionmaker=async_session_maker)
class ServiceAdmin(CustomModelAdmin):
    ServiceRequest.__name__ = "Услуги Заявки"

    schema_create = Service_requests_create
    schema_update = Service_requests_update

    model_repository = ServiceRequestRepository

    list_display = ("first_name", "last_name", "service", "phone")
    list_display_links = ("first_name", "last_name")
    list_filter = ("first_name", "last_name")

    search_fields = ("first_name", "last_name")
    raw_id_fields =("service_id", )

    fieldsets = ((None, {"fields": ("first_name", "last_name", "additional_contacts", "phone", "service")},),)
    formfield_overrides = {
        "first_name": (WidgetType.Input, {"required": True}),
        "last_name": (WidgetType.Input, {"required": True}),
        "additional_contacts": (WidgetType.TextArea, {"required": False}),
        "phone": (WidgetType.PhoneInput, {"required": True})
    }
