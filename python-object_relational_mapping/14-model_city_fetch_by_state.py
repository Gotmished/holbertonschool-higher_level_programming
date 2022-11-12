#!/usr/bin/python3
"""Module to list all City objects in hbtn_0e_6_usa"""

from model_state import Base, State
from model_city import City
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """Link class to table in database"""
    Session = sessionmaker()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session.configure(bind=engine)
    session = Session()

    for city, state in session.query(City, State).
    filter(City.state_id == State.id).order_by(City.id):
        print(f"{state.name}: ({city.id}) {city.name}")
