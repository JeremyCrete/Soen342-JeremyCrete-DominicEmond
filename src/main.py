from Controller.client_Controller import handle_client_menu  
from Controller.Instructor_Controller import handle_instructor_menu  
from Controller.admin_Controller import handle_admin_menu  
from create_tables import create_database 
from Controller.pickLesson_Controller import manage_user_lessons  
from database import engine, SessionLocal, Base, get_db  
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
            handle_client_menu() 
        elif choice == "2":
            print("Displaying Instructor menu")
            handle_instructor_menu()  
        elif choice == "3":
            print("Displaying Admin menu")
            handle_admin_menu()  
        elif choice == "4":
            print("Exiting program.")
            break  
        else:
            print("Invalid option. try again.")

if __name__ == "__main__":
    main()  