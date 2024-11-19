from sqlalchemy import Column, Integer, String, Boolean, Enum
from sqlalchemy.orm import relationship
from Model.Type import Type
from database import Base

class Offering(Base):
    __tablename__ = 'offerings'

    id = Column(Integer, primary_key=True, autoincrement=True)
    is_full = Column(Boolean, nullable=False)  # Using Boolean for clarity
    lesson_type = Column(Enum(Type), nullable=False)
    is_group_offering = Column(Boolean, nullable=False)  # Added field for group offerings
    group_size = Column(Integer, nullable=False)  # Define group size

    # Relationship to Booking: An offering can have many bookings
    bookings = relationship("Booking", back_populates="offering")

    def __init__(self, is_full, lesson_type, is_group_offering, group_size):
        self.is_full = is_full
        self.lesson_type = lesson_type
        self.is_group_offering = is_group_offering
        self.group_size = group_size  # Use group_size in initialization

    def __repr__(self):
        return f"Offering(id={self.id}, is_full={self.is_full}, lesson_type={self.lesson_type}, is_group_offering={self.is_group_offering}, group_size={self.group_size})"
