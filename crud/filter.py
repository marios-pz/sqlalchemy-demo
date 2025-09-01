from sqlalchemy.orm import Session, sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)

session = Session()


def print_users(users: list[User]):
    for user in users:
        print(f"[{user.name}] -> (Age: {user.age})")


print("\n### filter ###")

users_filter = session.query(User).filter(User.age >= 20, User.name == "Joey").all()
print("filtered users", len(users_filter))
print_users(users_filter)

print("\n### filter_by() ###")
users_filter_by = session.query(User).filter_by(age=30).all()
print("filtered users", len(users_filter_by))
print_users(users_filter_by)
