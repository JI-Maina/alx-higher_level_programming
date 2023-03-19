#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa via sqlalchemy
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    # create the engine
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # create table in database
    Base.metadata.create_all(engine)

    # create a session factory
    Session = sessionmaker(bind=engine)

    # create a session object
    session = Session()

    # query the data
    states = session.query(State).order_by(State.id).all()

    # display the data
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
