from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from Model import Instructor  # Ensure the Instructor model is imported
from database import engine  # Assuming you have an engine defined in database.py
from View.instructor_view import display_instructor_menu, get_instructor_choice
from Model import Lesson, InstructorAvailability

# Initialize the session maker
Session = sessionmaker(bind=engine)

def handle_instructor_menu():
    """Handles the menu for instructor-related operations."""
    while True:
        display_instructor_menu()  # Show the instructor menu
        choice = get_instructor_choice()  # Get the instructor's choice

        if choice == "1":
            select_available_lessons()
        elif choice == "2":
            register_instructor_in_cities()
        elif choice == "3":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def select_available_lessons():
    """Displays the available lessons."""
    session = Session()
    try:
        lessons = session.query(Lesson).filter(Lesson.mode == "active").all()
        if not lessons:
            print("No available lessons found.")
        else:
            print("Available Lessons:")
            for lesson in lessons:
                print(f"{lesson.id}. {lesson.mode} - {lesson.lesson_type}")
    except Exception as e:
        print(f"Error fetching lessons: {e}")
    finally:
        session.close()

def register_instructor_in_cities():
    """Allows an instructor to register their availability in cities."""
    session = Session()
    try:
        # Prompt the user for the instructor's name
        instructor_name = input("Enter your name: ").strip()

        # Check if the instructor exists in the database
        instructor = session.query(Instructor).filter(Instructor.name == instructor_name).first()

        if not instructor:
            print(f"No instructor found with the name '{instructor_name}'. Please register first.")
            return

        # Prompt the user for the cities they want to register for
        cities = input("Enter the cities where you're available (comma-separated): ").strip().split(',')

        # Insert each city into the Instructor_Availability table
        for city in cities:
            city = city.strip()
            try:
                instructor_availability = InstructorAvailability(instructor_id=instructor.id, city=city)
                session.add(instructor_availability)
                session.commit()
                print(f"Availability in '{city}' registered successfully.")
            except IntegrityError:
                print(f"Already registered availability in '{city}'. Skipping...")
                session.rollback()  # Rollback to continue with other inserts

    except Exception as e:
        print(f"Error registering availability: {e}")
    finally:
        session.close()
