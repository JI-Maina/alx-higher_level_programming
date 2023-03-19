#!/usr/bin/python3
"""Defines class State  and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state table"""

    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False,
                unique=True)
    name = Column(String(128), nullable=False)
