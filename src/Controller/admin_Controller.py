from sqlalchemy.orm import Session
from Controller.lesson_Controller import create_lesson
from Controller.cancelBooking import get_user_bookings, delete_booking
from View.admin_view import display_admin_menu, get_admin_choice
from database import SessionLocal


def handle_admin_menu():
    """
    Handles the admin menu actions.
    """
    while True:
        display_admin_menu()  # Display the admin menu
        choice = get_admin_choice()  # Get admin's choice

        if choice == "1":
            # Create a lesson
            create_lesson()

        elif choice == "2":
            # View and manage client bookings
            client_id = input("Enter the Client ID to view bookings: ")
            try:
                client_id = int(client_id)  # Ensure it's an integer
            except ValueError:
                print("Invalid Client ID. Please enter a valid number.")
                continue

            # Get user bookings
            bookings = get_user_bookings(client_id)
            if not bookings:
                print(f"No bookings found for Client ID {client_id}.")
                continue

            # Display bookings
            print("\n--- Bookings ---")
            for idx, booking in enumerate(bookings, start=1):
                print(f"{idx}. Booking ID: {booking.id}, Offering ID: {booking.offering_id}")

            # Ask if admin wants to delete a booking
            delete_choice = input("\nDo you want to delete a booking? (yes/no): ").strip().lower()
            if delete_choice == "yes":
                try:
                    booking_id_to_delete = input("Enter the Booking ID to delete: ")
                    booking_id_to_delete = int(booking_id_to_delete)  # Ensure it's an integer
                    delete_booking(client_id, booking_id_to_delete)
                except ValueError:
                    print("Invalid Booking ID. Please enter a valid number.")
            else:
                print("No bookings were deleted.")

        elif choice == "3":
            # Log out
            print("Logging out...")
            break

        else:
            print("Invalid option. Please try again.")


# Helper methods for database operations related to admin actions
def get_user_bookings(client_id: int):
    """
    Retrieves bookings for a given client.
    """
    session: Session = SessionLocal()
    try:
        # Query bookings for the given client
        bookings = session.execute(
            """
            SELECT b.id, b.offering_id
            FROM Booking b
            WHERE b.client_id = :client_id
            """,
            {"client_id": client_id}
        ).fetchall()
        return bookings
    except Exception as e:
        print(f"Error retrieving bookings: {e}")
        return []
    finally:
        session.close()


def delete_booking(client_id: int, booking_id: int):
    """
    Deletes a booking for a given client and booking ID.
    """
    session: Session = SessionLocal()
    try:
        # Delete the booking
        session.execute(
            """
            DELETE FROM Booking
            WHERE id = :booking_id AND client_id = :client_id
            """,
            {"booking_id": booking_id, "client_id": client_id}
        )
        session.commit()
        print(f"Booking ID {booking_id} deleted successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error deleting booking: {e}")
    finally:
        session.close()
    

from sqlalchemy.orm import Session
from Model.Lesson import Lesson  # Assuming Lesson model is defined correctly
from Model.Type import Type  # Assuming Type enum is already defined
from database import SessionLocal

def create_lesson():
    """
    Creates a new lesson by prompting the admin for necessary details.
    """
    # Gather lesson details from the admin
    print("\n--- Create a New Lesson ---")
    
    # Get lesson mode (private/group)
    mode = input("Enter lesson mode (private/group): ").strip().lower()
    while mode not in ['private', 'group']:
        print("Invalid mode. Please choose either 'private' or 'group'.")
        mode = input("Enter lesson mode (private/group): ").strip().lower()
    
    # Get lesson type (Yoga, Karate, etc.)
    print("\nAvailable lesson types: Yoga, Karate, Swimming, Dance")
    lesson_type_input = input("Enter lesson type: ").strip().upper()
    
    # Validate lesson type
    try:
        lesson_type = Type[lesson_type_input]  # Convert input to enum
    except KeyError:
        print(f"Invalid lesson type '{lesson_type_input}'. Please select from available lesson types.")
        return

    # Now that we have valid inputs, create the lesson
    session: Session = SessionLocal()
    try:
        new_lesson = Lesson(mode=mode, lesson_type=lesson_type)
        session.add(new_lesson)
        session.commit()
        print(f"Lesson '{lesson_type.name} ({mode})' created successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error creating lesson: {e}")
    finally:
        session.close()
