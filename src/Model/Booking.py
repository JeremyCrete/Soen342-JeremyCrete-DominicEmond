from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Booking(Base):
    __tablename__ = 'booking'  # Table name in the database

    bookingid = Column(Integer, primary_key=True, autoincrement=True)  # Primary key
    client_id = Column(Integer, ForeignKey('client.id'), nullable=False)  # Foreign key to Client table
    offering_id = Column(Integer, ForeignKey('offerings.id'), nullable=False)  # Foreign key to Offering table (note plural "offerings")

    # Relationships
    client = relationship("Client", back_populates="bookings")  # Back relationship to Client
    offering = relationship("Offering", back_populates="bookings")  # Back relationship to Offering

    def __init__(self, client_id, offering_id):
        self.client_id = client_id
        self.offering_id = offering_id

    def __eq__(self, other):
        if isinstance(other, Booking):
            return self.bookingid == other.bookingid
        return False
