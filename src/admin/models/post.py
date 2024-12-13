from fastadmin import WidgetType, register

from src.adapters.database.models import Post
from src.adapters.database.repositories import PostRepository
from src.adapters.database.session import async_session_maker
from src.admin.user_custom_fastadmin import CustomModelAdmin

from src.schemas.admin.posts import Posts_create, Posts_update


@register(Post, sqlalchemy_sessionmaker=async_session_maker)
class PostAdmin(CustomModelAdmin):
    Post.__name__ = "Посты"

    schema_create = Posts_create
    schema_update = Posts_update

    model_repository = PostRepository

    list_display = ("title", "channel", "text")
    list_display_links = ("title",)
    list_filter = ("title",)

    search_fields = ("title",)
    raw_id_fields = ("channel_id", )

    fieldsets = ((None, {"fields": ("channel", "title", "text", "image")},),)
    formfield_overrides = {
        "title": (WidgetType.Input, {"required": True}),
        "text": (WidgetType.TextArea, {"required": False}),
        "image": (WidgetType.Upload, {"required": False}),
    }
