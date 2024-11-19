def display_admin_menu():
    """
    Displays the admin menu options.
    """
    print("\n--- Admin Menu ---")
    print("1. Create Lesson")
    print("2. Manage Bookings")
    print("3. Logout")


def get_admin_choice():
    """
    Gets the admin's choice from the menu.
    """
    return input("\nSelect an option: ").strip()
