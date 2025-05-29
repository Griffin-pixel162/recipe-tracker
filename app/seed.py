from sqlalchemy.orm import sessionmaker
from models import Recipe, Base
from sqlalchemy import create_engine

engine = create_engine('sqlite:///recipe.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create sample recipes
recipe1 = Recipe(
    name="Spaghetti Carbonara",
    description="Classic Italian pasta dish",
    ingredients="Spaghetti, eggs, pancetta, parmesan, pepper",
    instructions="Boil pasta. Cook pancetta. Mix with eggs and cheese."
)

recipe2 = Recipe(
    name="Pancakes",
    description="Fluffy breakfast treat",
    ingredients="Flour, eggs, milk, sugar, butter",
    instructions="Mix ingredients. Cook on griddle until golden brown."
)

# Add and commit to database
session.add_all([recipe1, recipe2])
session.commit()

print("Sample recipes added to the database!")
