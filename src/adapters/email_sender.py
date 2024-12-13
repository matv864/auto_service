import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from smtplibaio import SMTP_SSL

from src.settings import settings


class SMTPClient:
    """
    Для Gmail:
    1. В настройках аккаунта добавить двухфакторную аутентификацию
    2. Создать приложение, назвать его как угоодно. https://myaccount.google.com/apppasswords?utm_source=google-account&utm_medium=web
    3. Получить пароль от gmail
    4. Вставить этот пароль в .env
    """

    def __init__(self, host: str = "smtp.gmail.com", port: int = 465):
        self.host = host
        self.port = port
        self.server = None

    async def __aenter__(self):
        self.server = SMTP_SSL(self.host, self.port)
        await self.server.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.server:
            await self.server.quit()

    async def login(self, username: str, password: str) -> None:
        if not self.server:
            raise ConnectionError("Connection error")
        await self.server.auth(username, password)

    async def send_email(
        self,
        from_addr: str,
        to_addresses: list,
        subject: str,
        body: str,
        content_type: str = "plain",
        attachments: list = [],
    ) -> None:
        """
        Отправляет письмо с возможностью прикрепления файлов.

        :param from_addr: str - Адрес отправителя.
        :param to_addresses: list - Список адресов получателей.
        :param subject: str - Тема письма.
        :param body: str - Текст письма (plain text или HTML).
        :param content_type: str - Тип содержимого ('plain' для текста, 'html' для HTML).
        :param attachments: list - Список файлов для прикрепления.
        """
        if not self.server:
            raise ConnectionError("Connection error")

        msg = MIMEMultipart()
        msg["From"] = from_addr
        msg["To"] = ", ".join(to_addresses)
        msg["Subject"] = subject
        msg.attach(MIMEText(body, content_type))

        if attachments:
            for file_path in attachments:
                if os.path.isfile(file_path):
                    with open(file_path, "rb") as file:
                        part = MIMEBase("application", "octet-stream")
                        part.set_payload(file.read())
                        encoders.encode_base64(part)
                        part.add_header(
                            "Content-Disposition",
                            f"attachment; filename={os.path.basename(file_path)}",
                        )
                        msg.attach(part)
                else:
                    raise FileNotFoundError(f"Файл {file_path} не найден")

        await self.server.sendmail(from_addr, to_addresses, msg.as_string())


class EmailSender:
    async def send_email(self, receivers: list[str], title: str, body: str) -> None:
        client = SMTPClient()
        async with client:
            await client.login(settings.MAIL_LOGIN, settings.MAIL_PASSWORD)
            await client.send_email(
                from_addr=settings.MAIL_LOGIN,
                to_addresses=receivers,
                subject=title,
                body=body
            )