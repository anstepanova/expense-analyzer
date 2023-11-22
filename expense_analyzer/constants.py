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
