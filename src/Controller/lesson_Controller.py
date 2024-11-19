from sqlalchemy.orm import Session
from Model import Lesson, Type as LessonType, Location, Timeslots, Instructor
from database import SessionLocal
from datetime import datetime


def new_lesson_to_offer(lesson_type_name: str, mode: bool):
    """
    Initialize a new lesson to offer.
    """
    session: Session = SessionLocal()
    try:
        # Get lesson type by name
        lesson_type = session.query(LessonType).filter_by(name=lesson_type_name).first()
        if not lesson_type:
            print(f"Lesson type '{lesson_type_name}' not found.")
            return None

        print(f"New lesson to offer initialized for type '{lesson_type_name}' and mode {'Online' if mode else 'In-Person'}.")
        return {"lesson_type_id": lesson_type.id, "mode": mode}
    except Exception as e:
        print(f"Error initializing new lesson: {e}")
    finally:
        session.close()


def find_location():
    """
    Find a suitable location for a lesson.
    """
    session: Session = SessionLocal()
    try:
        locations = session.query(Location).all()
        if not locations:
            print("No available locations.")
            return None

        print("\nAvailable Locations:")
        for idx, loc in enumerate(locations, start=1):
            print(f"{idx}. {loc.name} - {loc.city}, Capacity: {loc.capacity}")

        while True:
            choice = int(input("Select a location by number: "))
            if 1 <= choice <= len(locations):
                location = locations[choice - 1]
                print(f"Selected Location: {location.name}")
                return location
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"Error finding location: {e}")
    finally:
        session.close()


def specific_time():
    """
    Get a specific timeslot for a lesson.
    """
    session: Session = SessionLocal()
    try:
        timeslots = session.query(Timeslots).all()
        if not timeslots:
            print("No available timeslots.")
            return None

        print("\nAvailable Timeslots:")
        for idx, ts in enumerate(timeslots, start=1):
            print(f"{idx}. Start: {ts.start_time}, End: {ts.end_time}")

        while True:
            choice = int(input("Select a timeslot by number: "))
            if 1 <= choice <= len(timeslots):
                timeslot = timeslots[choice - 1]
                print(f"Selected Timeslot: {timeslot.start_time} - {timeslot.end_time}")
                return timeslot
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"Error selecting timeslot: {e}")
    finally:
        session.close()


def no_lesson_available():
    """
    Check if no lessons are available.
    """
    session: Session = SessionLocal()
    try:
        lessons = session.query(Lesson).all()
        if not lessons:
            print("No lessons available.")
            return True
        else:
            print(f"{len(lessons)} lessons are available.")
            return False
    except Exception as e:
        print(f"Error checking lesson availability: {e}")
    finally:
        session.close()


def create_lesson(lesson_type_name: str, mode: bool, start_date: str, end_date: str):
    """
    Create a new lesson with the provided details.
    """
    session: Session = SessionLocal()
    try:
        lesson_type = session.query(LessonType).filter_by(name=lesson_type_name).first()
        if not lesson_type:
            print(f"Lesson type '{lesson_type_name}' not found.")
            return

        location = find_location()
        if not location:
            return

        timeslot = specific_time()
        if not timeslot:
            return

        new_lesson = Lesson(
            lesson_type_id=lesson_type.id,
            mode=mode,
            start_date=start_date,
            end_date=end_date,
            location_id=location.id
        )
        session.add(new_lesson)
        session.commit()

        print(f"Lesson '{lesson_type_name}' created successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error creating lesson: {e}")
    finally:
        session.close()


def get_exact_schedule(lesson_id: int):
    """
    Retrieve the exact schedule for a lesson by its ID.
    """
    session: Session = SessionLocal()
    try:
        lesson = session.query(Lesson).filter_by(id=lesson_id).first()
        if not lesson:
            print(f"Lesson with ID {lesson_id} not found.")
            return None

        print(f"Lesson Schedule: Start Date: {lesson.start_date}, End Date: {lesson.end_date}")
        return {"start_date": lesson.start_date, "end_date": lesson.end_date}
    except Exception as e:
        print(f"Error retrieving schedule: {e}")
    finally:
        session.close()


def set_instructor(lesson_id: int, instructor_name: str):
    """
    Assign an instructor to a lesson.
    """
    session: Session = SessionLocal()
    try:
        lesson = session.query(Lesson).filter_by(id=lesson_id).first()
        if not lesson:
            print(f"Lesson with ID {lesson_id} not found.")
            return

        instructor = session.query(Instructor).filter_by(name=instructor_name).first()
        if not instructor:
            print(f"Instructor '{instructor_name}' not found.")
            return

        lesson.instructor_id = instructor.id
        session.commit()
        print(f"Instructor '{instructor_name}' assigned to Lesson ID {lesson_id}.")
    except Exception as e:
        session.rollback()
        print(f"Error assigning instructor: {e}")
    finally:
        session.close()
