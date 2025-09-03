from typing import override
from sqlalchemy import ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship, Mapped, mapped_column

db_url = "sqlite:///database.db"
engine = create_engine(db_url)

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(Integer, primary_key=True)


class FollowingAssociation(BaseModel):
    __tablename__ = "following_association"
    user_id: Mapped[Integer] = mapped_column(Integer, ForeignKey("users.id"))
    following_id: Mapped[Integer] = mapped_column(Integer, ForeignKey("users.id"))


class User(BaseModel):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(String)

    following = relationship(
        "User",
        secondary="following_association",
        primaryjoin=("FollowingAssociation.user_id==User.id"),
        secondaryjoin=("FollowingAssociation.following_id==User.id"),
    )

    @override
    def __repr__(self) -> str:
        return f"<User(id={self.id}, name={self.name}, following={self.following})>"


Base.metadata.create_all(engine)
