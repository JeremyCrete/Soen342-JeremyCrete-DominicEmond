from Controller.client_Controller import handle_client_menu  # Import the client controller
from Controller.Instructor_Controller import handle_instructor_menu  # Import the instructor controller
from Controller.admin_Controller import handle_admin_menu  # Import the admin controller
from create_tables import create_database  # Assuming you have a DatabaseSetup.py file to set up the DB
from Controller.pickLesson_Controller import manage_user_lessons  # Import the select lesson controller for client lesson management
from database import engine, SessionLocal, Base, get_db  # Import the necessary components
import logging

logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)

def main():
    create_database()  

    while True:
        print("\nLesson Management System")
        print("==============================")
        print("1. Client Menu")
        print("2. Instructor Menu")
        print("3. Admin Menu")
        print("4. Exit")
        
        choice = input("\nSelect an option: ")
        
        if choice == "1":
            print("Displaying Client menu")
            handle_client_menu()  #client menu 
        elif choice == "2":
            print("Displaying Instructor menu")
            handle_instructor_menu()  #instructor menu 
        elif choice == "3":
            print("Displaying Admin menu")
            handle_admin_menu()  #admin menu 
        elif choice == "4":
            print("Exiting program.")
            break  #Exit
        else:
            print("Invalid option. try again.")

if __name__ == "__main__":
    main()  