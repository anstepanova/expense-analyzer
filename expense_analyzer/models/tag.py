"""Describe Tag table which contain all transaction's tags."""
from typing import TYPE_CHECKING

from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped, relationship

from expense_analyzer.constants import DbConstants
from expense_analyzer.models.associations import transaction_tag_association
from expense_analyzer.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from expense_analyzer.models.transaction import Transaction


class Tag(TimestampMixin, DbConstants.BASE):
    """Contain information about tags."""

    tag: Mapped[str] = Column(String(length=15), nullable=False, unique=True)
    transactions: Mapped[list['Transaction']] = relationship(
        secondary=transaction_tag_association,
        back_populates='tags_for_transaction',
    )
