from typing import override
from sqlalchemy import ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    declarative_base,
    mapped_column,
    relationship,
    sessionmaker,
)

db_url = "sqlite:///posts.db"
engine = create_engine(db_url, echo=True)


Session = sessionmaker(bind=engine)
session = Session()


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__: str = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    posts = relationship("Post", lazy="select", backref="user")

    @override
    def __repr__(self) -> str:
        return f"<User {self.name}>"


class Post(Base):
    __tablename__: str = "posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    content: Mapped[str] = mapped_column(String)
    user_id = mapped_column(Integer, ForeignKey("users.id"))

    @override
    def __repr__(self) -> str:
        return f"<Post {self.id}>"


Base.metadata.create_all(engine)


user = User(
    name="Joey Jordison", posts=[Post(content=f"content for {x}") for x in range(1, 5)]
)

session.add(user)
session.commit()

print("Accessing User")
print(user)
print("Accessing Posts specifically")
print(user.posts)
