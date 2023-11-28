#!/usr/bin/python3
'''
Module to create State model class
to be used as an Object mapper
'''


from sqlalchemy import declarative_base,\
      Column, Integer, String, create_engine
from sys import argv

if __name__ == '__main__':
    engine = create_engine(f'mysql+mysqldb://\
                        {argv[1]}:{argv[2]}\
                        :3306@localhost')
    Base = declarative_base()

    class State(Base):
        '''
        State base model
        '''

        __tablename__ = "states"

        id = Column(Integer,
                    autoincrement=True,
                    nullable=False,
                    unique=True,
                    primary_key=True)

        name = Column(String(128),
                      nullable=False)

    Base.metadata.create_all(engine)
