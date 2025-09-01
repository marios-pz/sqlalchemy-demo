from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

db_url = "sqlite:///database.db"

engine = create_engine(db_url)

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id: Column[int] = Column(Integer, primary_key=True)
    name: Column[str] = Column(String)
    age: Column[int] = Column(Integer)


Base.metadata.create_all(engine)
