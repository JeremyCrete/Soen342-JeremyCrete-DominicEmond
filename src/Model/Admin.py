from sqlalchemy import Column, Integer, String
from database import Base  # Import Base from your database setup file

class Admin(Base):
    __tablename__ = 'admins'  # The name of the table in the database

    # Columns
    id = Column(Integer, primary_key=True, autoincrement=True)  # Primary key, auto-incremented
    username = Column(String, unique=True, nullable=False)  # Username, unique and not nullable
    password = Column(String, nullable=False)  # Password, not nullable

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"Admin(username={self.username}, password={self.password})"

    def __eq__(self, other):
        if isinstance(other, Admin):
            return self.username == other.username and self.password == other.password
        return False
