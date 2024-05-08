from pony.orm import DatabaseError

from .models import db


def init_database():
    try:
        db.bind(provider='postgres', user='postgres', password='password', host='localhost', database='SMW_database')
        db.generate_mapping(create_tables=True)
    except DatabaseError as e:
        # Log the error or handle it as needed
        print(f"Error occurred during database initialization: {e}")
        # Optionally, re-raise the exception to propagate it further
        raise
