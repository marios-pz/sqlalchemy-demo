import random

from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()

# names = ["Andrew", "Stefan", "Mario", "Eloy", "Joey"]
# ages = [20, 21, 22, 23, 24]
#
# for x in range(20):
#     user = User(name=random.choice(names), age=random.choice(ages))
#     session.add(user)
#
# session.commit()


# ascending
# users = session.query(User).order_by(User.age).all()

# descending + order by name
users = session.query(User).order_by(User.age.desc(), User.name).all()

for user in users:
    print(f"{user.name}, {user.age}")
