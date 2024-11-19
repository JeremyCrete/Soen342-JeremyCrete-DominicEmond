from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from Model import Instructor  # Ensure the Instructor model is imported
from database import engine  # Assuming you have an engine defined in database.py
from View.instructor_view import display_instructor_menu, get_instructor_choice
from Model import Lesson, InstructorAvailability
from datetime import date

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
            register_instructor()
        elif choice == "3":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def select_available_lessons():
    """Displays the available lessons."""
    session = Session()
    try:
        # You can adjust this query to fetch lessons by any condition, for example:
        lessons = session.query(Lesson).all()  # Fetch all lessons, not just 'active'
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


def register_instructor():
    """Register a new instructor with their credentials and specialization."""
    session = Session()
    try:
        # Prompt for the instructor's details
        instructor_name = input("Enter your name: ").strip()
        phone_number = input("Enter your phone number: ").strip()
        specialization = input("Enter your specialization: ").strip()

        # Prompt for start and end dates
        start_date_str = input("Enter your start date (YYYY-MM-DD): ").strip()
        end_date_str = input("Enter your end date (YYYY-MM-DD): ").strip()

        # Convert input dates to date objects
        try:
            start_date = date.fromisoformat(start_date_str)
            end_date = date.fromisoformat(end_date_str)
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
            return

        # Create the new instructor object and add it to the session
        new_instructor = Instructor(
            name=instructor_name,
            phone_number=phone_number,
            start_date=start_date,
            end_date=end_date,
            specialization=specialization
        )
        session.add(new_instructor)
        session.commit()
        print(f"Instructor {instructor_name} added successfully!")

    except IntegrityError as e:
        print(f"Error: {e}")
        session.rollback()  # Ensure that the session is rolled back on error
    except Exception as e:
        print(f"Error registering instructor: {e}")
    finally:
        session.close()
