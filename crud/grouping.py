from sqlalchemy.orm import Session, sessionmaker
from models import User, engine
from sqlalchemy import func

Session = sessionmaker(bind=engine)

session = Session()

# group users by age
# users = session.query(User.name, func.count(User.id)).group_by(User.name).all()
# print(users)


# chaining

users = (
    session.query(User.age, func.count(User.id))
    .filter(User.age > 24)
    .order_by(User.age)
    .filter(User.age < 50)
    .group_by(User.age)
    .all()
)

for user in users:
    print(user)
