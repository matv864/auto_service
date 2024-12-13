import os

from fastapi import APIRouter
from fastapi.responses import FileResponse


filestorage_router = APIRouter()


@filestorage_router.get("/public/{filename}",)
async def get_channels(filename: str):
    filepath = f"public/{filename}"
    if os.path.isfile(filepath):
        return FileResponse(
            path=filepath,
            filename=filename,
            media_type="application/octet-stream"
        )
    else:
        return None