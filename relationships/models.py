from typing import override
from sqlalchemy import ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship, Mapped, mapped_column

db_url = "sqlite:///database.db"
engine = create_engine(db_url)

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True)


class Address(BaseModel):
    __tablename__ = "address"

    city: Mapped[str] = mapped_column(String)
    state: Mapped[str] = mapped_column(String)
    zip_code: Mapped[int] = mapped_column(Integer)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    @override
    def __repr__(self) -> str:
        return f"<Address(id={self.id}, city={self.city})>"


class User(BaseModel):
    __tablename__ = "users"
    name: Mapped[str] = mapped_column(String)
    age: Mapped[int] = mapped_column(Integer)
    addresses: Mapped[list["Address"]] = relationship(
        "Address", backref="user"
    )  # backwards relationship

    following_id = mapped_column(Integer, ForeignKey("users.id"))
    following = relationship("User", remote_side=[id], uselist=True)

    @override
    def __repr__(self) -> str:
        return f"<User(id={self.id}, name={self.name})>"


Base.metadata.create_all(engine)
