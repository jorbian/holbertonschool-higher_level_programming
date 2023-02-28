#!/usr/bin/python3
""" LISTS 'state' OBJECT WITH NAME PASSED AS ARG """

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        state = session.query(State).order(State.id).filter(
                State.name == sys.argv[4]
            ).one()
        print(state.id)
    except Exception:
        print("Not found")
