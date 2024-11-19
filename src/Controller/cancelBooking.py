from sqlalchemy.orm import Session
from Model import Booking, Offering
from database import SessionLocal


def get_user_bookings(client_id: int):
    """
    Retrieve and display bookings for a specific client.
    """
    session: Session = SessionLocal()
    try:
        # Query to fetch bookings
        bookings = (
            session.query(Booking, Offering)
            .join(Offering, Booking.offering_id == Offering.id)
            .filter(Booking.client_id == client_id)
            .all()
        )

        if not bookings:
            print("No bookings found for this client.")
            return []

        print("\nClient's Bookings:")
        for index, (booking, offering) in enumerate(bookings, start=1):
            print(f"{index}. Offering ID: {offering.id}, Full: {offering.isFull}")

        return bookings
    except Exception as e:
        print(f"Error retrieving bookings: {e}")
        return []
    finally:
        session.close()


def delete_booking(client_id: int, offering_id: int):
    """
    Delete a booking for a specific client and offering.
    """
    session: Session = SessionLocal()
    try:
        # Check if the booking exists
        booking = (
            session.query(Booking)
            .filter_by(client_id=client_id, offering_id=offering_id)
            .first()
        )

        if not booking:
            print("No such booking found for this client.")
            return

        # Delete the booking
        session.delete(booking)

        # Mark the offering as available again
        offering = session.query(Offering).filter_by(id=offering_id).first()
        if offering:
            offering.isFull = False

        session.commit()

        print(f"Booking with Offering ID {offering_id} deleted successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error deleting booking: {e}")
    finally:
        session.close()


def handle_cancel_booking(client_id: int):
    """
    Handle the process of displaying and canceling a booking for a client.
    """
    # Step 1: Display bookings
    bookings = get_user_bookings(client_id)

    if not bookings:
        return

    # Step 2: Select a booking to delete
    print("\nWhich booking would you like to cancel?")
    for index, (booking, offering) in enumerate(bookings, start=1):
        print(f"{index}. Offering ID: {offering.id}")

    try:
        selection = int(input("Enter the number of the booking to cancel: "))
        if 1 <= selection <= len(bookings):
            selected_booking = bookings[selection - 1][1]  # Get the Offering object
            delete_booking(client_id, selected_booking.id)
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input. Please enter a number.")
