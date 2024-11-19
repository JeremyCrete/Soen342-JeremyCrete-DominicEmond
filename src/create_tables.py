from database import Base, engine
from Model import Booking, Lesson, Location, Offering, Schedule, Timeslot, Instructor, Client, InstructorAvailability

def create_database():
    print("Starting database creation...")
    try:
        # Create all tables in the engine (this will create tables in your SQLite database)
        Base.metadata.create_all(bind=engine)
        print("Tables created successfully.")
    except Exception as e:
        print(f"Error creating tables: {e}")


create_database()