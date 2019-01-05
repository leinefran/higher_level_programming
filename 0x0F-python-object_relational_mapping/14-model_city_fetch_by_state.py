#!/usr/bin/python3
"""a script that lists all cities objects from the database hbtn_0e_14_usa"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, ForeignKey



if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    all_c = session.query(City, State).filter(City.state_id == State.id).all()
    for c, s in all_c:
        print('{}: ({}) {}'.format(s.name, c.id, c.name))
