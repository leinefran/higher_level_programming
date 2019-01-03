#!/usr/bin/python3
'''
module 'base_model'
'''

import models
import SQLAlchemy

Base = declarative_base()

class State(Base):
    '''
    Class definition of a state.
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name =  Column(String(128))

    # Create an engine to the census database
    user = sys.argv[1]
    password = sys.argv[2]

    engine = create_engine('mysql+mysqlconnector://user:password@localhost:3306/states')
