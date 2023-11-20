"""Describe User table."""

from sqlalchemy import Column, String

from expense_analyzer.constants import DbConstants
from expense_analyzer.models.mixins import TimestampMixin


class User(TimestampMixin, DbConstants.BASE):
    """Contain information about users."""
    username = Column(String(length=256), nullable=False)
    email = Column(String(length=256), nullable=False, unique=True)
