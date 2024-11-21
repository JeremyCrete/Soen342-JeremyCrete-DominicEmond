from Model.Type import Type
from Model.VenueType import VenueType
from database import SessionLocal
from Model import Client, Instructor, Lesson, Location, Offering
from datetime import date

def seed_clients():
    """Add some sample clients to the database."""
    client_data = [
        {"name": "Jake Doe", "phone_number": "123-456-7890", "age": 38},
        {"name": "Jeremy Crete", "phone_number": "514-324-3054", "age": 21},
        {"name": "Teddy Smith", "phone_number": "345-345-2312", "age": 26},
    ]
    session = SessionLocal()
    for client in client_data:
        new_client = Client(**client)
        session.add(new_client)
    session.commit()
    print(f"Seeded {len(client_data)} clients.")

def seed_instructors():
    """Add some sample instructors to the database."""
    instructor_data = [
        {"name": "Stephanie Crete", "phone_number": "524-234-1234", "start_date": date(2022, 5, 1), "end_date": date(2024, 5, 1), "specialization": "Yoga"},
        {"name": "Louis Brown", "phone_number": "364-938-8294", "start_date": date(2021, 6, 1), "end_date": date(2023, 6, 1), "specialization": "Karate"},
    ]
    session = SessionLocal()
    for instructor in instructor_data:
        new_instructor = Instructor(**instructor)
        session.add(new_instructor)
    session.commit()
    print(f"Seeded {len(instructor_data)} instructors.")

def seed_lessons():
    """Add some sample lessons to the database."""
    lesson_data = [
        {"mode": "group", "lesson_type": Type.YOGA, "is_active": True},
        {"mode": "private", "lesson_type": Type.KARATE, "is_active": True},
    ]
    session = SessionLocal()
    for lesson in lesson_data:
        new_lesson = Lesson(**lesson)  # Pass the dictionary with the correct keys
        session.add(new_lesson)
    session.commit()
    print(f"Seeded {len(lesson_data)} lessons.")



def seed_locations():
    """Add some sample locations to the database."""
    location_data = [
        {"name": "Downtown Studio", "city": "Montreal", "address": "123 Main St", "capacity": 20, "venue_type": "Studio"},
        {"name": "Central Gym", "city": "Montreal", "address": "456 Gym Rd", "capacity": 50, "venue_type": "Gym"},
    ]
    session = SessionLocal()
    for location in location_data:
        new_location = Location(**location)
        session.add(new_location)
    session.commit()
    print(f"Seeded {len(location_data)} locations.")

def seed_offerings():
    """Add some sample offerings to the database."""
    offering_data = [
        {"is_full": False, "is_group_offering": True, "lesson_type": Type.YOGA, "group_size": 2},  # Group lesson
        {"is_full": False, "is_group_offering": False, "lesson_type": Type.KARATE, "group_size": 1},  # Private lesson
        {"is_full": False, "is_group_offering": True, "lesson_type": Type.SWIMMING, "group_size": 2},  # Group lesson
        {"is_full": False, "is_group_offering": False, "lesson_type": Type.DANCE, "group_size": 1},  # Private lesson
    ]
    session = SessionLocal()
    for offering in offering_data:
        new_offering = Offering(**offering)
        session.add(new_offering)
    session.commit()
    print(f"Seeded {len(offering_data)} offerings.")



def seed_database():
    """Seed the database with initial data."""
    seed_clients()
    seed_instructors()
    seed_lessons()
    seed_locations()
    seed_offerings()

if __name__ == "__main__":
    seed_database()
