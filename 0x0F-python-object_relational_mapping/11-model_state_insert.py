#!/usr/bin/python3
"""adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State

    # create engine
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # create table in db
    Base.metadata.create_all(engine)

    # create a session factory
    Session = sessionmaker(bind=engine)

    # create a session object
    session = Session()
    name = 'Louisiana'

    state = State()
    state.name = name

    # add and persist new state to the database
    session.add(state)
    session.commit()

    state_id = session.query(State).filter(State.name == name).first()
    print(state.id)

    session.close()
