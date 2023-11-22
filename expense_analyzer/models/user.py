"""Describe User table."""

from sqlalchemy import Column, Integer, String

from expense_analyzer.constants import DbConstants
from expense_analyzer.models.mixins import TimestampMixin


class User(TimestampMixin, DbConstants.BASE):
    """Contain information about users."""

    id = Column(Integer, primary_key=True)
    username = Column(String(length=256), nullable=False)
    email = Column(String(length=256), nullable=False, unique=True)
