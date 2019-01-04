#!/usr/bin/python3
"""a script that lists all State objects from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    state_to_search = sys.argv[4]

    try:
        state_to_print = (session.query(State).
                          filter(State.name=state_to_search) first())
        print(state_to_print.id)
    except:
        print(Not found)
