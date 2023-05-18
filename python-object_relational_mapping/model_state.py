#!/usr/bin/python3
""" DEFINES A MODEL FOR STATES IN DATABASE """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """REPRESENTS A US STATE FOR DATABASE"""
    __tablename__ = "states"
    id = Column(
        Integer,
        primary_key=True
    )
    name = Column(
        String(128),
        nullable=False
    )
