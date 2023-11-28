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

    with Session(bind=eng) as session:
        results = session.query(City.id, City.name, State.name)\
                         .join(State)\
                         .order_by(City.id)
        for result in results:
            print(f"{result[0]}: {result[1]} -> {result[2]}")
