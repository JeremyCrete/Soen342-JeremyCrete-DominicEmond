from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from Model import Client, Offering, Lesson, Schedule, Timeslot, Location
from database import engine  # Assuming you have an engine defined in database.py
from Model import Booking

# Initialize the session maker
Session = sessionmaker(bind=engine)

def manage_user_lessons(user_id):
    session = Session()
    try:
        # Fetch available lessons from the database
        available_lessons = session.query(Lesson).join(Offering).filter(Offering.is_full == False).all()

        if not available_lessons:
            print("No available lessons found.")
        else:
            print("Available Lessons and Time Slots:")
            for idx, lesson in enumerate(available_lessons, start=1):
                lesson_type = lesson.lesson_type
                mode = "Online" if lesson.mode else "In-person"
                print(f"{idx}. {lesson.id} - {lesson_type} | Mode: {mode}")
                # For each lesson, print more details like schedule, location, etc.
                for offering in lesson.offerings:
                    location = offering.location.name
                    availability = "Available" if not offering.is_full else "Full"
                    print(f"    Offering at {location}: {availability}")

            # User selects a lesson to enroll in
            choice = int(input("Select the lesson number to enroll in: ")) - 1
            selected_lesson = available_lessons[choice]

            # Get the offering from the selected lesson
            selected_offering = None
            for offering in selected_lesson.offerings:
                if not offering.is_full:
                    selected_offering = offering
                    break

            if selected_offering:
                # Proceed with booking the lesson
                book_lesson(selected_offering, user_id, session)
            else:
                print("No available slots for the selected lesson.")

        session.commit()

    except Exception as e:
        print(f"Error selecting lesson: {e}")
    finally:
        session.close()


def book_lesson(offering, user_id, session):
    try:
        # Create a new booking
        new_booking = Booking(client_id=user_id, offering_id=offering.id)
        session.add(new_booking)
        
        # Update the offering to mark it as full
        offering.is_full = True
        session.commit()

        print(f"Booking successful! Your booking ID is {new_booking.bookingid}.")

    except Exception as e:
        print(f"Error booking the lesson: {e}")
        session.rollback()
