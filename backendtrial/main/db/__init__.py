# backend/db/__init__.py

from .models import db

def init_db():
    db.bind(provider='postgres', user='postgres', password='sonal1999', host='localhost', database='SMW')
    db.generate_mapping(create_tables=True)
