from sqlalchemy import Column, Integer, String, Boolean, Enum
from sqlalchemy.orm import relationship
from Model.Type import Type
from database import Base

class Offering(Base):
    __tablename__ = 'offerings'  # Changed to plural for consistency

    id = Column(Integer, primary_key=True, autoincrement=True)
    is_full = Column(Boolean, nullable=False)  # Using Boolean for clarity
    lesson_type = Column(Enum(Type), nullable=False)
    is_group_offering = Column(Boolean, nullable=False)  # Added field for group offerings

    # Relationship to Booking: An offering can have many bookings
    bookings = relationship("Booking", back_populates="offering")  # This links with the `offering` relationship in Booking

    def __init__(self, is_full, lesson_type, is_group_offering):
        self.is_full = is_full
        self.lesson_type = lesson_type
        self.is_group_offering = is_group_offering

    def __repr__(self):
        return f"Offering(id={self.id}, is_full={self.is_full}, lesson_type={self.lesson_type}, is_group_offering={self.is_group_offering})"
