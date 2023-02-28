#!/usr/bin/python3
"""
DELETES ALL 'States' with 'name' CONTAINING SPECIFIED LETTER FROM DATABASE
'hbtn_0e_6_usa.'
"""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":

    target_letter = "a"

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

    for state in session.query(State):
        if target_letter in state.name:
            session.delete(state)

    session.commit()
