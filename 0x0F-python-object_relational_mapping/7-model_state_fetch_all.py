#!/usr/bin/python3
"""
This script lists alltate objects
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state importtate, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
ession = sessionmaker(bind=engine)

    session =ession()

    for instance in session.query(State).order_by(State.id):
        print('{0}: {1}'.format(instance.id, instance.name))
