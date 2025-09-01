from random import randint
from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)

session = Session()

# Create users
user1 = User(name="Joey Jordison")
user2 = User(name="Eloy Casagrande")
user3 = User(name="El Estepario")


# Follows
user1.following.append(user2)
user2.following.append(user3)
user3.following.append(user1)

session.add_all([user1, user2, user3])
session.commit()

print(user1)
print(user2)
print(user3)
