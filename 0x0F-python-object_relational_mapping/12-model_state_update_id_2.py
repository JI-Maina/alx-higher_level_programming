#!/usr/bin/python3
"""changes the name of a State object from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    # create engine
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # create tables in db
    Base.metadata.create_all(engine)

    # create session factory
    Session = sessionmaker(bind=engine)

    # create session object
    session = Session()

    # retieve state to update and update
    state = session.query(State).filter(State.id == 2).first()

    state.name = 'New Mexico'

    # add and persist changes to db
    session.add(state)
    session.commit()

    session.close()
