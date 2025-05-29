from sqlalchemy import create_engine
from models import Base

# Connect to SQLite database (creates file if it doesn't exist)
engine = create_engine('sqlite:///recipe.db')

# Create all tables defined in models.py
Base.metadata.create_all(engine)

print("Database and 'recipes' table created!")
