#!/usr/bin/python3
"""
Module containing the class definition of State
and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """
    Creating the State class as a child of Base.
    Relationship established with child City class
    including reference from city object to state
    object being named 'state'
    """
    __tablename__ = "states"

    id = Column(Integer, nullable=False, primary_key=True,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        backref="state",
        cascade="all, delete"
        )
