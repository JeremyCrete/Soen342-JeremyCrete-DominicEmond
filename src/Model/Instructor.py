# In the instructor.py file

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from database import Base
from Model.InstructorAvailability import InstructorAvailability  # Make sure this import is before Instructor

class Instructor(Base):
    __tablename__ = 'instructors'  # Table name in the database

    # Columns
    id = Column(Integer, primary_key=True, autoincrement=True)  # Primary key, auto-incremented
    name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    specialization = Column(String, nullable=False)

    # Relationship to InstructorAvailability
    availabilities = relationship("InstructorAvailability", back_populates="instructor")


    def __init__(self, name, phone_number, start_date, end_date, specialization):
        self.name = name
        self.phone_number = phone_number
        self.start_date = start_date
        self.end_date = end_date
        self.specialization = specialization

    def __repr__(self):
        return f"Instructor(name={self.name}, phone_number={self.phone_number}, start_date={self.start_date}, end_date={self.end_date}, specialization={self.specialization})"

    def __eq__(self, other):
        if isinstance(other, Instructor):
            return (self.name == other.name and
                    self.phone_number == other.phone_number and
                    self.start_date == other.start_date and
                    self.end_date == other.end_date and
                    self.specialization == other.specialization)
        return False
