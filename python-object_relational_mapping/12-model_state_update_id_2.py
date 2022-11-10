#!/usr/bin/python3
"""Module to change the name of a State object in hbtn_0e_6_usa"""

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

    try:
        change_name = session.query(State).filter(State.id == 2).first()
        change_name.name = 'New Mexico'
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()

    session.close()
