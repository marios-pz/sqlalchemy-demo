from random import randint
from sqlalchemy.orm import sessionmaker
from models import Address, User, engine

Session = sessionmaker(bind=engine)

session = Session()

# Create users
age: int = randint(1, 100)
user1 = User(name="Joey Jordison", age=age)

age = randint(1, 100)
user2 = User(name="Eloy Casagrande", age=age)

# Addresses

address1 = Address(city="City A", state="CA", zip_code="10001")
address2 = Address(city="City B", state="CB", zip_code="10021")
address3 = Address(city="City C", state="CC", zip_code="10031")

user1.addresses.extend([address1, address2])
user2.addresses.append(address3)

session.add(user1)
session.add(user2)
session.commit()

print(f"{user1.addresses =}")
print(f"{user2.addresses =}")
print(f"{address1.user =}")
