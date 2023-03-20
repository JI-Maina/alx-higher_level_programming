#!/usr/bin/python3
"""prints the State object with the name passed as argument from the database
hbtn_0e_6_usa"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State

    # create engine
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # create table in database
    Base.metadata.create_all(engine)

    # create a session factory
    Session = sessionmaker(bind=engine)

    # create session object
    session = Session()

    # query data
    state = session.query(State).filter(State.name == argv[4]).first()

    if state is None:
        print('Not found')
    else:
        print(state.id)
