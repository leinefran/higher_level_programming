#!/usr/bin/python3
'''
module 'base_model'
'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    '''
    Class definition of a state.
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name =  Column(String(128))
