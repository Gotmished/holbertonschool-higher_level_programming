#!/usr/bin/python3
"""
Module to add City object 'San Francisco' and  State object
'California' to hbtn_0e_10_usa making use of 'state' backref
in parent State class
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

    city_state_add = City(name="San Francisco", state=State(name="California"))
    try:
        session.add(city_state_add)
    except Exception:
        session.rollback()
        raise
    else:
        session.commit()
