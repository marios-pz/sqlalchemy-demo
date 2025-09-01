from sqlalchemy.orm import Session, sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)

session = Session()


def add_query() -> None:
    user = User(name="Amogus", age=30)
    session.add(User(name="giorgos potsephs", age=69))
    session.add(user)
    session.commit()


def filter_query():
    user = session.query(User).filter_by(age=69).all()
    print(user)


def main() -> None:
    filter_query()


main()
