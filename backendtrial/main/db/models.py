# backend/db/models.py

from pony.orm import Database, Required

db = Database()

class User(db.Entity):
    email = Required(str, unique=True)
    password = Required(str)
    company = Required(str)
    username = Required(str)
    isAdmin = Required(bool, default=False)  # Add isAdmin column with default value
