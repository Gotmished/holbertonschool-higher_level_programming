#!/usr/bin/python3
"""
Module to print all State and City objects in hbtn_0e_101_usa.
No need for filter to link two separate classes now due to
cities relationship (used for all State objects)
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    """Link class to table in database"""
    Session = sessionmaker()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session.configure(bind=engine)
    session = Session()
    import_records = session.query(State).order_by(
            State.id).all()
    for state in import_records:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")
