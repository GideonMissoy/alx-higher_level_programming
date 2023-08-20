#!/usr/bin/python3

"""
Script prints all `City` objects from the database
`hbtn_0e_14_usa`.
"""

from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    citate = session.query(City, State).join(State)
    for city, state in citate.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
