from sqlalchemy import Column, Integer, String
from database import Base  # Import Base from your database setup file

class Schedule(Base):
    __tablename__ = 'schedules'  # The name of the table in the database

    # Columns
    id = Column(Integer, primary_key=True, autoincrement=True)  # Primary key, auto-incremented
    start_date = Column(String, nullable=False)  # String to store the start date
    end_date = Column(String, nullable=False)  # String to store the end date

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f"Schedule(start_date={self.start_date}, end_date={self.end_date})"

    def __eq__(self, other):
        if isinstance(other, Schedule):
            return self.start_date == other.start_date and self.end_date == other.end_date
        return False
