"""Contain types to use as the base for the generated declarative base
class."""
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declared_attr

__all__ = (
    'Base',
)


class Base:
    """Base for declarative base class."""

    id = Column(Integer, primary_key=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
