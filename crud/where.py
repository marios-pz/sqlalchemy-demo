from sqlalchemy.orm import Session, sessionmaker
from models import User, engine

from sqlalchemy import or_, and_, not_

Session = sessionmaker(bind=engine)

session = Session()


def print_users(users: list[User]):
    for user in users:
        print(f"[{user.name}] -> (Age: {user.age})")


# where by default does AND
# users = session.query(User).where(User.age >= 24, User.name == "Joey").all()


users = session.query(User).where(and_(User.age >= 24, User.name == "Joey")).all()

# bitwise AND
users = session.query(User).where((User.age >= 24) & (User.name == "Joey")).all()
print("\n AND")
print_users(users)


# where OR
users = session.query(User).where(or_(User.age >= 24, User.name == "Joey")).all()

# bitwise OR
users = session.query(User).where((User.age >= 24) | (User.name == "Joey")).all()
print("\n OR")
print_users(users)


# where NOT
users = session.query(User).where(not_(User.name == "Joey")).all()
print("\n NOT")
print_users(users)
