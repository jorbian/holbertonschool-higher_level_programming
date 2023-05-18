#!/usr/bin/python3
""" DEFINES OBJECT MODEL FOR CITY IN MYSQL TABLE """

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """ REPRESENTS CITY IN DATABASE """
    __tablename__ = "cities"
    id = Column(
        Integer,
        primary_key=True
    )
    name = Column(
        String(128),
        nullable=False
    )
    state_id = Column(
        Integer,
        ForeignKey("states.id"),
        nullable=False
    )
