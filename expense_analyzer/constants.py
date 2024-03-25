"""Application constants."""
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base

from expense_analyzer.config import services_settings
from expense_analyzer.db_base_types import Base


class DbConstants:
    """Constants for the database."""
    ENGINE = create_async_engine(
        str(services_settings.async_postgres_dsn), connect_args={"check_same_thread": False},
    )
    BASE = declarative_base(cls=Base)


class RouterPrefixConstants:
    V1 = '/v1'
    CURRENCY = '/currency'


class RouterTagConstants:
    V1_TAGS = ['v1']
    CURRENCY_TAGS = ['currency']


class PathParametersDefaultValues:
    SKIP_ITEMS_FOR_PAGINATION = 0
    LIMIT_ITEMS_FOR_PAGINATION = 100
