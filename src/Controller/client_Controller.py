from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from Model import Client, Offering, Booking, Lesson # Import SQLAlchemy models
from database import engine  # Assuming you have an engine defined in database.py
from View.client_view import client_choice, client_menu

# Initialize the session maker
Session = sessionmaker(bind=engine)

def handle_client_menu():
    while True:
        client_menu()
        choice = client_choice()

        if choice == "1":
            view_available_lessons()
        elif choice == "2":
            age = input("Enter your age: ")
            try:
                age = int(age)
                if age < 18:
                    print("You must be 18 or older to create a booking. Returning to the menu.")
                    continue  # Return to the menu if not old enough
            except ValueError:
                print("Invalid age. Please enter a numeric value.")
                continue

            # If age verification passes, proceed with booking
            client_id = input("\nEnter your client ID: ")
            try:
                user_id = int(client_id)  # Ensure the input is valid
                book_offer(user_id)  # Pass the validated user ID to the booking function
            except ValueError:
                print("Invalid client ID. Please enter a numeric value.")

        elif choice == "3":
            view_my_bookings()
        elif choice == "4":
            client_id = input("\nEnter your client ID: ")
            try:
                user_id = int(client_id)  # Ensure the input is valid
                manage_user_lessons(user_id)
            except ValueError:
                print("Invalid client ID. Please enter a numeric value.")
        elif choice == "5":
            client_id = input("\nEnter your Client ID: ")
            try:
                user_id = int(client_id)
                get_user_bookings(client_id)
                offering_id = input("\nEnter offering ID: ")
                delete_booking(user_id, offering_id)
            except ValueError:
                print("Invalid Client ID")
        elif choice == "6":
            print("\nAdd a New Client")
            name = input("Enter your name: ")
            phone_number = input("Enter your phone number: ")
            age = input("Enter your age: ")
            try:
                age = int(age)  # Validate age as an integer
                if age < 0:
                    print("Age cannot be negative.")
                else:
                    # Call the function to add the client to the database
                    add_client_to_database(name, phone_number, age)
            except ValueError:
                print("Invalid age. Please enter a numeric value.")

        elif choice == "7":
            print("Logging out...")
            break
        else:
            print("Invalid option. Please try again.")

def add_client_to_database(name, phone_number, age):
    """Add a new client to the database."""
    session = Session()
    try:
        # Create a new client and add to the session
        new_client = Client(name=name, phone_number=phone_number, age=age)
        session.add(new_client)
        session.commit()
        print(f"Client {name} added successfully!")
    except Exception as e:
        print(f"Error adding client: {e}")
    finally:
        session.close()

def view_available_lessons():
    """Fetch and display available lessons."""
    session = Session()
    try:
        offerings = session.query(Offering).all()  # Fetch all offerings
        if not offerings:
            print("No available lessons found.")
        else:
            print("Available Lessons:")
            for offering in offerings:
                status = "Available" if not offering.is_full else "Full"
                lesson_mode = "Group" if offering.is_group_offering else "Private"
                # Check the number of people already booked for group lessons
                if offering.is_group_offering:
                    booked_count = session.query(Booking).filter(Booking.offering_id == offering.id).count()
                    status = "Available" if booked_count < offering.group_size else "Full"
                    print(f"{offering.id}. {lesson_mode} - {offering.lesson_type} (Booked: {booked_count}/{offering.group_size})")
                else:
                    print(f"{offering.id}. {lesson_mode} - {offering.lesson_type} ({status})")
    except Exception as e:
        print(f"Error fetching lessons: {e}")
    finally:
        session.close()




def book_lesson(client_id):
    """Book a lesson."""
    lesson_id = input("\nEnter the lesson ID to book: ")

    session = Session()
    try:
        lesson = session.query(Offering).filter(Offering.id == lesson_id).first()
        if lesson and not lesson.is_full:
            # Check if the group size has been reached
            bookings_count = session.query(Booking).filter(Booking.offering_id == lesson_id).count()
            if bookings_count >= lesson.group_size:
                lesson.is_full = True
                session.commit()
                print("This lesson is no longer available.")
            else:
                # Create a new booking
                new_booking = Booking(client_id=client_id, offering_id=lesson_id)
                session.add(new_booking)
                session.commit()

                # Update the lesson availability if it's now full
                if bookings_count + 1 >= lesson.group_size:
                    lesson.is_full = True
                    session.commit()

                print(f"Booking successful! Your booking ID is {new_booking.bookingid}.")
        else:
            print("This lesson is no longer available.")
    except Exception as e:
        print(f"Error booking lesson: {e}")
    finally:
        session.close()




def view_my_bookings():
    """Display bookings for the client."""
    client_id = input("\nEnter your client ID to view bookings: ")

    session = Session()
    try:
        bookings = session.query(Booking).join(Offering).filter(Booking.client_id == client_id).all()
        if not bookings:
            print("You have no bookings.")
        else:
            print("Your Bookings:")
            for booking in bookings:
                print(f"Booking ID {booking.bookingid}: {booking.offering.lesson_type} ({'Group' if booking.offering.is_group_offering else 'Private'})")
    except Exception as e:
        print(f"Error fetching bookings: {e}")
    finally:
        session.close()



def book_offer(client_id):
    """Book a lesson for the client."""
    lesson_id = input("\nEnter the lesson ID to book: ")

    session = Session()
    try:
        lesson = session.query(Offering).filter(Offering.id == lesson_id).first()
        if lesson and not lesson.is_full:
            # Create a new booking
            new_booking = Booking(client_id=client_id, offering_id=lesson_id)
            session.add(new_booking)
            session.commit()

            # Update the lesson availability
            lesson.is_full = True
            session.commit()

            print(f"Booking successful! Your booking ID is {new_booking.bookingid}.")
        else:
            print("This lesson is no longer available.")
    except Exception as e:
        print(f"Error booking lesson: {e}")
    finally:
        session.close()

def manage_user_lessons(user_id):
    """Manage lessons booked by the user (view/edit lesson details)."""
    session = Session()
    try:
        lessons = session.query(Lesson).filter(Lesson.client_id == user_id).all()  # Assuming 'client_id' is a field in Lesson model
        if not lessons:
            print("You have no lessons to manage.")
        else:
            print("Your Lessons:")
            for lesson in lessons:
                print(f"Lesson ID: {lesson.id} - {lesson.mode} - {lesson.lesson_type}")
                # You can add further management options here if necessary
    except Exception as e:
        print(f"Error managing lessons: {e}")
    finally:
        session.close()

def get_user_bookings(client_id):
    """Fetch and display bookings for a specific client."""
    session = Session()
    try:
        # Query bookings for the given client_id
        bookings = session.query(Booking).join(Offering).filter(Booking.client_id == client_id).all()
        
        if not bookings:
            print("No bookings found for this client.")
        else:
            print(f"Bookings for Client ID {client_id}:")
            for booking in bookings:
                print(f"Booking ID: {booking.bookingid} - Lesson Type: {booking.offering.lesson_type} - Status: {'Full' if booking.offering.is_full else 'Available'}")
    except Exception as e:
        print(f"Error fetching bookings: {e}")
    finally:
        session.close()


def delete_booking(user_id, offering_id):
    """Delete a booking for a specific client and offering."""
    session = Session()
    try:
        # Query the booking based on client_id and offering_id
        booking_to_delete = session.query(Booking).filter(
            Booking.client_id == user_id,
            Booking.offering_id == offering_id
        ).first()

        if booking_to_delete:
            # Delete the booking
            session.delete(booking_to_delete)
            session.commit()
            print(f"Booking {booking_to_delete.bookingid} has been successfully deleted.")
            
            # Optionally, make the offering available again
            offering = session.query(Offering).filter(Offering.id == offering_id).first()
            if offering:
                offering.is_full = False  # Make the offering available again
                session.commit()
                print(f"Offering {offering_id} is now available.")
        else:
            print(f"No booking found for client ID {user_id} and offering ID {offering_id}.")
    
    except Exception as e:
        print(f"Error deleting booking: {e}")
    
    finally:
        session.close()
