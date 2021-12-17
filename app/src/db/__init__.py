"""
The main entry point for Relational Database in MySQL!
Amer Ahmed
Alexander Amaechi
Abshir Mohamed
Elvir Velagic
Supervisor: Joakim Wassberg
Version 0.0.1
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# MYSQL CONNECTION
engine = create_engine(f"mysql+mysqlconnector://root:Myservername@localhost:3306/manufacturing")
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
