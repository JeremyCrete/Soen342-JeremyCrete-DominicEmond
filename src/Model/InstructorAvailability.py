# In the instructor_availability.py file

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class InstructorAvailability(Base):
    __tablename__ = 'instructor_availability'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    instructor_id = Column(Integer, ForeignKey('instructors.id'), nullable=False)
    city = Column(String, nullable=False)
    
    # Relationship to Instructor
    instructor = relationship("Instructor", back_populates="availabilities")

    def __init__(self, instructor_id, city):
        self.instructor_id = instructor_id
        self.city = city

    def __repr__(self):
        return f"InstructorAvailability(instructor_id={self.instructor_id}, city={self.city})"
