from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from Model import Client  # Import the Client model
from database import engine  # Assuming you have an engine defined in database.py

# Initialize the session maker
Session = sessionmaker(bind=engine)

def add_client_to_database(name, phone_number, age):
    """Adds a new client to the Client table."""
    session = Session()
    try:
        # Create a new client instance and add to the session
        new_client = Client(name=name, phone_number=phone_number, age=age)
        session.add(new_client)
        session.commit()  # Commit the transaction
        print(f"Client added successfully with ID: {new_client.id}")
        return new_client.id  # Return the client ID for further use if needed
    except Exception as e:
        print(f"Error adding the client: {e}")
        session.rollback()  # Rollback in case of error
    finally:
        session.close()

