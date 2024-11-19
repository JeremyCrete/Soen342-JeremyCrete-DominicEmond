from sqlalchemy.orm import Session
from Model import Offering, Booking, Client, LessonType, Location, Instructor
from database import SessionLocal


def get_available_offerings(session: Session):
    """
    Fetch and display available offerings from the database.
    """
    offerings = (
        session.query(Offering, LessonType, Location, Instructor)
        .join(LessonType, Offering.lesson_type_id == LessonType.id)
        .join(Location, Offering.location_id == Location.id)
        .join(Instructor, Offering.instructor_id == Instructor.id)
        .filter(Offering.isFull == False)
        .all()
    )

    if offerings:
        print("\nAvailable Offerings:")
        for index, (offering, lesson_type, location, instructor) in enumerate(offerings, start=1):
            print(f"{index}. {lesson_type.name} at {location.name} with {instructor.name}")

        while True:
            try:
                selection = int(input("\nPlease select an offering by number: "))
                if 1 <= selection <= len(offerings):
                    selected_offering = offerings[selection - 1][0]  # Get the selected Offering object
                    return selected_offering.id
                else:
                    print("Invalid selection. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    else:
        print("\nNo available offerings.")
        return None


def create_booking(client_id: int, offering_id: int, session: Session):
    """
    Create a booking for a client and mark the offering as full.
    """
    try:
        # Check if the offering is still available
        offering = session.query(Offering).filter_by(id=offering_id, isFull=False).first()

        if not offering:
            print("Selected offering is no longer available.")
            return

        # Create a new booking
        new_booking = Booking(client_id=client_id, offering_id=offering_id)
        session.add(new_booking)

        # Mark the offering as full
        offering.isFull = True

        # Commit the transaction
        session.commit()

        print(f"Booking created successfully for client {client_id} and offering {offering_id}.")

    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")


def book_offer(user_id: int):
    """
    Handles the process of booking an offering for a client.
    """
    session = SessionLocal()

    try:
        # Get available offerings
        offering_id = get_available_offerings(session)

        # If an offering was selected, proceed to book
        if offering_id is not None:
            create_booking(user_id, offering_id, session)
        else:
            print("No available offerings to book.")
    finally:
        session.close()
