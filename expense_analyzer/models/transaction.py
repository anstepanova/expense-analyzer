"""Describe Transaction table."""
from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from expense_analyzer.constants import DbConstants
from expense_analyzer.models.associations import transaction_tag_association
from expense_analyzer.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from expense_analyzer.models.currency import Currency
    from expense_analyzer.models.tag import Tag
    from expense_analyzer.models.user import User


class Transaction(TimestampMixin, DbConstants.BASE):
    """Contain information about tags."""

    amount: Mapped[float] = Column(Float, nullable=False)
    currency_id: Mapped[int] = mapped_column((ForeignKey('currency.id')))
    currency: Mapped['Currency'] = relationship(back_populates='transactions_for_currency')
    tag: Mapped[list['Tag']] = relationship(
        secondary=transaction_tag_association,
        back_populates='transactions_for_tag',
    )
    is_income: Mapped[bool] = Column(Boolean, nullable=False)
    comment: Mapped[str] = Column(String(256), default=None)
    date: Mapped[date] = Column(Date, server_default=func.now())
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped['User'] = relationship(back_populates='transactions')
