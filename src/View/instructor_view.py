def display_instructor_menu():
    """Displays the instructor menu with options."""
    print("\n--- Instructor Menu ---")
    print("1. Select Available Lessons")
    print("2. Register Instructor Availability in Cities")
    print("3. Log Out")

def get_instructor_choice():
    """Gets the instructor's choice from the menu."""
    return input("\nSelect an option: ")

def display_lessons(lessons):
    """Displays the list of available lessons."""
    if not lessons:
        print("No available lessons found.")
    else:
        print("Available Lessons:")
        for lesson in lessons:
            print(f"{lesson.id}. {lesson.mode} - {lesson.lesson_type}")

def display_error(message):
    """Displays an error message."""
    print(f"Error: {message}")
