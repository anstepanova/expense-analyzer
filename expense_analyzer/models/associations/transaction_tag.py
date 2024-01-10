"""Describe the association table for many-to-many relationship between tag and
transaction tables."""
from sqlalchemy import Column, ForeignKey, Table

from expense_analyzer.constants import DbConstants

transaction_tag_association = Table(
    'transaction_tag_association',
    DbConstants.BASE.metadata,
    Column('transaction_id', ForeignKey('transaction.id'), primary_key=True),
    Column('tag_id', ForeignKey('tag.id'), primary_key=True),
)
