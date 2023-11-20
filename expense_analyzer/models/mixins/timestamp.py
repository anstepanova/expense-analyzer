"""Make Timestamp Mixin for sqlalchemy models.

The mixin contains updated_at, created_at fields
"""

from sqlalchemy import Column, DateTime, func


class TimestampMixin:
    """Timestamp mixin which timestamp information to a table.

    updated_at: the datetime when the row was updated
    created_at: the datetime when the row was created
    """
    updated_at = Column(DateTime, onupdate=func.now(), server_default=func.now(), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
