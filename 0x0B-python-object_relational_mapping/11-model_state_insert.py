#!/usr/bin/python3
""" ADDS 'state' OBJECT 'Lousiana' to DATABASE 'hbtn_0e_6_usa.' """

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":

    new_state_name = "Louisiana"

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

    new_state = State(name=new_state_name)
    
    session.add(new_state)
    session.commit()

    print(new_state.id)
