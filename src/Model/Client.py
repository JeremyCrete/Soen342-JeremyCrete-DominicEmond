from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    # Relationship to Booking: A client can have many bookings
    bookings = relationship("Booking", back_populates="client")  # This links with the `client` relationship in Booking

    def __init__(self, name, phone_number, age):
        self.name = name
        self.phone_number = phone_number
        self.age = age

    def __repr__(self):
        return f"Client(name={self.name}, phone_number={self.phone_number}, age={self.age})"
