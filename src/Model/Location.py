from sqlalchemy import Column, Integer, String, Enum
from database import Base
from Model.VenueType import VenueType  # Import your Enum

class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    address = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    venue_type = Column(Enum(VenueType), nullable=False)  # Use the VenueType Enum here

    def __init__(self, name, city, address, capacity, venue_type):
        self.name = name
        self.city = city
        self.address = address
        self.capacity = capacity
        self.venue_type = venue_type

    def __repr__(self):
        return f"Location(name={self.name}, city={self.city}, address={self.address}, capacity={self.capacity}, venue_type={self.venue_type})"
