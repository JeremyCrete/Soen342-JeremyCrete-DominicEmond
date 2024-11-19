# client_view.py

def client_menu():
    """Display the menu options for the client."""
    print("\n----- Client Menu -----")
    print("1. View All Available Lessons")
    print("2. Book Lesson")
    print("3. View Bookings")
    print("4. Manage Lessons")
    print("5. Delete Booking")
    print("6. Register as a New Client")
    print("7. Log Out From System")

def client_choice():
    """Prompt the user to select an option from the menu."""
    return input("\nSelect an option (1-7): ")

def display_lessons(lessons):
    """Display the list of lessons."""
    print("\nAvailable Lessons:")
    if not lessons:
        print("No available lessons found.")
    else:
        for lesson in lessons:
            print(f"{lesson.id}. {lesson.mode} - {lesson.lesson_type}")
        
def display_bookings(bookings):
    """Display the list of bookings for a client."""
    print("\nYour Bookings:")
    if not bookings:
        print("You have no bookings.")
    else:
        for booking in bookings:
            print(f"Booking ID {booking.bookingid}: {booking.offering.lesson_type} - {booking.offering.location.name}")
        
def confirm_action(action_message):
    """Confirm an action with the user."""
    confirm = input(f"{action_message} (y/n): ").lower()
    if confirm == 'y':
        return True
    return False
