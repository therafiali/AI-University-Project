from sqlalchemy import String, Integer, Column, Boolean, ForeignKey
from database import Base, engine
from sqlalchemy.orm import Mapped, registry, mapped_column
from typing import List
from sqlalchemy.orm import relationship
from database import Session
from pydantic import BaseModel

def create_tables():
    """
    Creates all tables in the database.
    """
    Base.metadata.create_all(engine)

session = Session()


class University(Base):
    __tablename__ = 'university'
    # id = Column(Integer, primary_key=True, index=True)
    # name = Column(String,nullable=False)
    id:Mapped[int] = mapped_column(primary_key=True),
    name:Mapped[str] = mapped_column(nullable=False)
    programs = relationship('Program', backref='university')

class Program(Base):
    __tablename__ = 'programs'
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    university_id = Column(String, ForeignKey('university.id'))
    courses = relationship('Course', backref='program')

class Course(Base):
    __tablename__ = 'courses'
    id = Column(String, primary_key=True,index=True)
    name = Column(String)
    program_id = Column(String, ForeignKey('programs.id'))
    # Assuming Topic, Student, and Instructor are other SQLAlchemy models
    # topics = relationship('Topic', backref='course')
    # students = relationship('Student', backref='course')
    # instructors = relationship('Instructor', backref='course')
    
class OurBaseModel(BaseModel):
    # class Config:
    #     orm_mode = True
    class Config:
        from_attributes = True    
    
    
class Uni(OurBaseModel):
    name: str
    
    
        
uni = University(id=3,name='AI University')    
session.add(uni)
session.commit()

