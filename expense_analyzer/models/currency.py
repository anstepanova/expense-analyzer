"""Describe Currency table with exchange rates to the nominate currency."""
from typing import TYPE_CHECKING

from sqlalchemy import Column, Float, String
from sqlalchemy.orm import Mapped, relationship

from expense_analyzer.constants import DbConstants
from expense_analyzer.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from expense_analyzer.models.transaction import Transaction


class Currency(TimestampMixin, DbConstants.BASE):
    """Contain information about available currencies and its exchange
    rates."""
    name: Mapped[str] = Column(String(length=5), nullable=False, unique=True)
    exchange_rate_to_nominate_currency: Mapped[float] = Column(Float, nullable=False)
    transactions: Mapped[list['Transaction']] = relationship(back_populates='tags_for_transaction')
