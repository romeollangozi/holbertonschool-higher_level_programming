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

    all_rows = session.query(State).all()
    for row in all_rows:
        print(f"{row.id}: {row.name}")
        for city in row.cities:
            print(f"    {city.id}: {city.name}")
    session.close()
    eng.dispose()
