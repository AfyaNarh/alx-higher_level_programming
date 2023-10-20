#!/usr/bin/python3
"""
This script adds thetate object
`Louisiana` to the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state importtate, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get a state
    from the database.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
ession = sessionmaker(bind=engine)

    session =ession()

    new_state =tate(name="Louisiana")
    session.add(new_state)
    session.commit()

    print('{0}'.format(new_state.id))
    session.close()
