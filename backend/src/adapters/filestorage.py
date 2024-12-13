import os
from io import BytesIO
from uuid import uuid4
from mimetypes import guess_extension

from src.settings import settings


class FilestorageGateway:
    def get_file_url(self, filename: str):
        return f"{settings.BACKEND_DOMAIN}/public/{filename}"

    def upload_file(self, file: BytesIO, mimetype: str) -> str:
        flag_to_break = False
        while not flag_to_break:
            new_filename = str(uuid4())
            for busy_filename in os.listdir("public"):
                if new_filename in busy_filename:
                    break
            else:
                flag_to_break = True

        extension = guess_extension(mimetype)
        full_filename = f"{new_filename}{extension}"

        with open(f"public/{full_filename}", "wb") as f:
            f.write(file.getbuffer())

        return full_filename

    def delete_file(self, filename: str) -> None:
        filepath = f"public/{filename}"
        if os.path.isfile(filepath):
            os.remove(filepath)