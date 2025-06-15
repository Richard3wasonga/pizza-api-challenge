import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from server.app import app
from server.models import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza
from faker import Faker
from random import randint, choice as rc

fake = Faker()

pizza_names = [
    "Margherita", "Pepperoni", "BBQ Chicken", "Hawaiian", "Veggie",
    "Four Cheese", "Buffalo Chicken", "Meat Lovers", "Supreme"
]

ingredients_list = [
    "Tomato Sauce, Mozzarella, Basil",
    "BBQ Sauce, Chicken, Onion, Cilantro",
    "Ham, Pineapple, Mozzarella",
    "Peppers, Onions, Mushrooms, Olives",
    "Mozzarella, Parmesan, Ricotta, Gorgonzola",
    "Sausage, Pepperoni, Bacon, Ham",
    "Hot Sauce, Chicken, Blue Cheese",
    "Ground Beef, Pepperoni, Bacon, Onion",
    "Spinach, Tomato, Garlic, Feta"
]

with app.app_context():
    print("Seeding...")

    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()

    restaurants = [Restaurant(name=fake.company(), address=fake.address()) for _ in range(5)]
    db.session.add_all(restaurants)

    pizza_data = list(zip(pizza_names, ingredients_list))
    pizzas = [Pizza(name=name, ingredients=ingredients) for name, ingredients in pizza_data]
    db.session.add_all(pizzas)
    db.session.commit()

    restaurant_pizzas = []
    for _ in range(15):
        pizza = rc(pizzas)
        restaurant = rc(restaurants)

        rp = RestaurantPizza(
            price=randint(5, 30),
            pizza_id=pizza.id,
            restaurant_id=restaurant.id
        )
        restaurant_pizzas.append(rp)

    db.session.add_all(restaurant_pizzas)
    db.session.commit()
    print("Done seeding.")
