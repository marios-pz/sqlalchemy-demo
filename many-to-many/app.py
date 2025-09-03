from random import randint
from sqlalchemy import Column, ForeignKey, String, Integer, Table, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_url = "sqlite:///database.db"
engine = create_engine(db_url)

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()


# student_course_link = Table(
#     "student_course",
#     Base.metadata,
#     Column("student_id", Integer, ForeignKey("students.id")),
#     Column("course_id", Integer, ForeignKey("courses.id")),
# )


class StudentCourse(Base):
    __tablename__ = "student_courses"
    id = Column(Integer, primary_key=True)
    student_id = Column("student_id", Integer, ForeignKey("students.id"))
    course_id = Column("course_id", Integer, ForeignKey("courses.id"))


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship(
        "Course", secondary="student_courses", back_populates="students"
    )


class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    students = relationship(
        "Student", secondary="student_courses", back_populates="courses"
    )


Base.metadata.create_all(engine)

math = Course(title="Mathematical Analysis 1")
prog = Course(title="Computer Programming")
eloy = Student(name="Eloy Casagrande", courses=[math, prog])
joey = Student(name="Joey Jordison", courses=[math])


session.add_all([math, prog, eloy, joey])
session.commit()
