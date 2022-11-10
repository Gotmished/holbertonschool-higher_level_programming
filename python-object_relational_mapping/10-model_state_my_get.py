#!/usr/bin/python3
"""
Module to print a State object from hbtn_0e_6_usa
based upon user input
"""

from model_state import Base, State
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

    state = session.query(State).filter(State.name == '%s' % argv[4]).first()
    if state:
        print(state.id)
    else:
        print("Not found")
