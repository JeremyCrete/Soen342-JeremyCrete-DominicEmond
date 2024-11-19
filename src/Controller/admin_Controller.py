from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from Controller.lesson_Controller import create_lesson
from Controller.cancelBooking import delete_booking
from View.admin_view import display_admin_menu, get_admin_choice
from database import SessionLocal
from Model import Booking, Lesson, Instructor, Client
from Model.Type import Type
from Model.Offering import Offering


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
                print(f"{idx}. Booking ID: {booking.bookingid}, Offering ID: {booking.offering_id}")

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
    Retrieves bookings for a given client and prints the client's name and lesson details.
    """
    session = SessionLocal()  # Create a session
    try:
        # Query bookings for the given client and join with the Offering and Client tables to get lesson details
        bookings = session.query(Booking).join(Offering).join(Client).filter(Booking.client_id == client_id).all()
        
        if not bookings:
            print(f"No bookings found for Client ID {client_id}.")
            return []

        # Fetch client details
        client = session.query(Client).filter(Client.id == client_id).first()

        print(f"Bookings for Client: {client.name} (Client ID {client.id}):")
        for booking in bookings:
            offering = booking.offering  # Get the offering object from the booking
            lesson_type = offering.lesson_type
            mode = "Group" if offering.is_group_offering else "Private"
            print(f"Booking ID: {booking.bookingid}, Offering: {offering.id}, Lesson Type: {lesson_type}, Mode: {mode}")

        return bookings  # Return the bookings and offering data

    except Exception as e:
        print(f"Error retrieving bookings: {e}")
        return []
    finally:
        session.close()  # Always close the session




def delete_booking(client_id: int, booking_id: int):
    """
    Deletes a booking for a given client and booking ID.
    """
    session: Session = SessionLocal()
    try:
        # Delete the booking
        session.execute(
            """
            DELETE FROM booking
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


def delete_client(client_id: int):
    """
    Deletes a client from the database.
    """
    session: Session = SessionLocal()
    try:
        # Delete the client from the Client table
        session.execute(
            """
            DELETE FROM client
            WHERE id = :client_id
            """,
            {"client_id": client_id}
        )
        session.commit()
        print(f"Client ID {client_id} deleted successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error deleting client: {e}")
    finally:
        session.close()


def delete_instructor(instructor_id: int):
    """
    Deletes an instructor from the database.
    """
    session: Session = SessionLocal()
    try:
        # Delete the instructor from the Instructor table
        session.execute(
            """
            DELETE FROM instructor
            WHERE id = :instructor_id
            """,
            {"instructor_id": instructor_id}
        )
        session.commit()
        print(f"Instructor ID {instructor_id} deleted successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error deleting instructor: {e}")
    finally:
        session.close()


# Helper methods for creating a lesson (using the `create_lesson` from Controller)
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
