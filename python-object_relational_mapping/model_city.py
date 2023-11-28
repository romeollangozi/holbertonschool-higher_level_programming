#!/usr/bin/python3
'''
Module to create City model class
to be used as an Object mapper
'''


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    '''
    State base model
    '''

    __tablename__ = "cities"

    id = Column(Integer,
                autoincrement=True,
                nullable=False,
                unique=True,
                primary_key=True)

    name = Column(String(128),
                  nullable=False)

    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
