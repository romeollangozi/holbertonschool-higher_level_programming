#!/usr/bin/python3
"""
Start link class to table in database
"""


import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(
                                sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True
                        )
    Base.metadata.create_all(eng)

    session = Session(bind=eng)
    session.begin()
    new_state = State(name="California")
    session.add(new_state)
    session.commit()
    new_city = City(name="San Francisco", state_id=new_state.id)
    session.add(new_city)
    session.commit()
    session.close()
