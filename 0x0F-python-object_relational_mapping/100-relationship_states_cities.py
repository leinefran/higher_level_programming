#!/usr/bin/python3
"""a script that creates the State “California” with the
City “San Francisco” from the database hbtn_0e_100_usa"""

import sys
import sqlalchemy
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from relationship_city import City

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    ca = State(name="California", cities=[City(name="San Francisco")])
    session.add(ca)
    session.commit()
    session.close()
