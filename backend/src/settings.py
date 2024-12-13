from functools import cached_property

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    BACKEND_DOMAIN: str

    POSTGRES_HOST: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    MAIL_LOGIN: str
    MAIL_PASSWORD: str

    @cached_property
    def postgres_url(self):
        return (
            "postgresql+asyncpg://"
            + f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            + f"{self.POSTGRES_HOST}/{self.POSTGRES_DB}"
        )


settings = Settings()  # type: ignore
