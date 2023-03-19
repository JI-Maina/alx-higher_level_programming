#!/usr/bin/python3
"""prints the first State object from the database hbtn_0e_6_usa
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

    # create table in the database
    Base.metadata.create_all(engine)

    # create a session factory
    Session = sessionmaker(bind=engine)

    # create a session object
    session = Session()

    # query the data
    state = session.query(State).first()

    if state is None:
        print()
    else:
        print(f"{state.id}: {state.name}")

    session.close()
