from sqlalchemy import Column, Integer, String
from database import Base  # Import Base from your database setup file

class Timeslot(Base):
    __tablename__ = 'timeslots'  # The name of the table in the database

    # Columns
    id = Column(Integer, primary_key=True, autoincrement=True)  # Primary key, auto-incremented
    start_time = Column(String, nullable=False)  # String to store the start time
    end_time = Column(String, nullable=False)  # String to store the end time

    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"Timeslot(start_time={self.start_time}, end_time={self.end_time})"

    def __eq__(self, other):
        if isinstance(other, Timeslot):
            return self.start_time == other.start_time and self.end_time == other.end_time
        return False
