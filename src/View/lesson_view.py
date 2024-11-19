def display_lesson_menu():
    """
    Display the menu for lesson-related operations.
    """
    print("\n--- Lesson Menu ---")
    print("1. Create a Lesson")
    print("2. View All Lessons")
    print("3. Back to Admin Menu")

def get_lesson_choice():
    """
    Get the admin's choice from the lesson menu.
    """
    return input("\nSelect an option: ")

def display_available_lessons(lessons):
    """
    Display all available lessons to the user.
    :param lessons: List of lessons to display
    """
    if not lessons:
        print("No lessons available.")
    else:
        print("\n--- Available Lessons ---")
        for lesson in lessons:
            print(f"Lesson ID: {lesson.id}")
            print(f"Type: {lesson.lesson_type.name}")
            print(f"Mode: {'Online' if lesson.mode else 'In-Person'}")
            print(f"Start Date: {lesson.start_date}")
            print(f"End Date: {lesson.end_date}")
            print("-" * 20)

def get_lesson_details():
    """
    Get details from the admin to create a lesson.
    :return: A dictionary containing lesson details
    """
    lesson_type = input("Enter the lesson type (e.g., Yoga, Karate, etc.): ").strip()
    mode = input("Is the lesson online? (yes/no): ").strip().lower() == "yes"
    start_date = input("Enter the lesson start date (YYYY-MM-DD): ").strip()
    end_date = input("Enter the lesson end date (YYYY-MM-DD): ").strip()
    location_id = input("Enter the Location ID: ").strip()
    timeslot_id = input("Enter the TimeSlot ID: ").strip()
    
    return {
        "lesson_type": lesson_type,
        "mode": mode,
        "start_date": start_date,
        "end_date": end_date,
        "location_id": int(location_id),
        "timeslot_id": int(timeslot_id),
    }
