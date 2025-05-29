from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Recipe, Base

# Connect to database
engine = create_engine('sqlite:///recipe.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create all tables
Base.metadata.create_all(engine)

def menu():
    while True:
        print("\nRecipe Tracker")
        print("1. View all recipes")
        print("2. Add a new recipe")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            view_recipes()
        elif choice == '2':
            add_recipe()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

def view_recipes():
    recipes = session.query(Recipe).all()
    if not recipes:
        print("No recipes found.")
    for recipe in recipes:
        print(f"\nID: {recipe.id}")
        print(f"Name: {recipe.name}")
        print(f"Description: {recipe.description}")
        print(f"Ingredients: {recipe.ingredients}")
        print(f"Instructions: {recipe.instructions}")

def add_recipe():
    name = input("Enter recipe name: ")
    description = input("Enter description: ")
    ingredients = input("Enter ingredients (comma-separated): ")
    instructions = input("Enter instructions: ")
    
    new_recipe = Recipe(
        name=name,
        description=description,
        ingredients=ingredients,
        instructions=instructions
    )
    session.add(new_recipe)
    session.commit()
    print(f"Recipe '{name}' added successfully!")

if __name__ == '__main__':
    menu()
