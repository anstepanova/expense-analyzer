"""Describe User table."""

from typing import TYPE_CHECKING

from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, relationship

from expense_analyzer.constants import DbConstants
from expense_analyzer.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from expense_analyzer.models.transaction import Transaction


class User(TimestampMixin, DbConstants.BASE):
    """Contain information about users."""

    username: Mapped[str] = Column(String(length=256), nullable=False, unique=True)
    email: Mapped[str] = Column(String(length=256), nullable=False, unique=True)
    transactions: Mapped[list['Transaction']] = relationship(back_populates="user")
