from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

# Database setup
DATABASE_URL = "sqlite:///recipe.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
