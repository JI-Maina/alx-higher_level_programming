#!/usr/bin/python3
"""lists all State objects that contain the letter a from the database
hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State

    # create an engine
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # create table in database
    Base.metadata.create_all(engine)

    # create a session factory
    Session = sessionmaker(bind=engine)

    # create session object
    session = Session()

    # create a query
    states = session.query(State)\
        .filter(State.name.like('%a%')).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
