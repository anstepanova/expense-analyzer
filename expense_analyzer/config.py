"""Load and validate configuration from .env files and the environment
variables."""


from os.path import join
from pathlib import Path

from pydantic import BaseModel, Field, IPvAnyAddress, PostgresDsn, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig:
    """Configuration of the application."""

    BASE_DIR = Path(__file__).resolve().parent.parent
    "attribute BASE_DIR base directory of the project"
    ENV_FILE_PATH_FROM_ROOT_DIRECTORY = 'docker/.env'
    ENV_FILE_ABSOLUTE_PATH = join(BASE_DIR, ENV_FILE_PATH_FROM_ROOT_DIRECTORY)


class EnvSettings(BaseSettings):
    """Settings taken from environment file or the environment variables."""
    model_config = SettingsConfigDict(env_file=AppConfig.ENV_FILE_ABSOLUTE_PATH, extra='ignore')

    db_host: str
    postgres_port: str
    postgres_user: str
    postgres_password: SecretStr
    db_password: SecretStr
    db_user: str
    db_name: str
    app_port: str = Field(validation_alias='app_private_port')
    app_host: IPvAnyAddress = Field(validation_alias='app_host')


class ServicesSettings(BaseModel):
    """Setting for other services.

    For example: redis, postgres, etc
    """
    postgres_dsn: PostgresDsn


class AppSettings(BaseModel):
    """Application settings."""
    port: str
    host: IPvAnyAddress


env_settings = EnvSettings()
services_settings = ServicesSettings(
    postgres_dsn=f'postgres://{env_settings.postgres_user}@{env_settings.db_host}:{env_settings.postgres_port}/'
                 f'{env_settings.db_name}',
)
app_setting = AppSettings(
    port=env_settings.app_port,
    host=env_settings.app_host,
)
