from fastadmin import WidgetType, register

from src.adapters.database.models import Gallery
from src.adapters.database.repositories import GalleryRepository
from src.adapters.database.session import async_session_maker
from src.admin.user_custom_fastadmin import CustomModelAdmin

from src.schemas.admin.gallery import Gallery_create, Gallery_update


@register(Gallery, sqlalchemy_sessionmaker=async_session_maker)
class PostAdmin(CustomModelAdmin):
    Gallery.__name__ = "Галерея"

    schema_create = Gallery_create
    schema_update = Gallery_update

    model_repository = GalleryRepository

    list_display = ("name", "changing_date")
    list_display_links = ("name",)
    list_filter = ("name",)

    search_fields = ("name",)
    readonly_fields = ("changing_date", )

    fieldsets = ((None, {"fields": ("name", "image", "changing_date")},),)
    formfield_overrides = {
        "name": (WidgetType.Input, {"required": False}),
        "image": (WidgetType.Upload, {"required": True}),
    }
