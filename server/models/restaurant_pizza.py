from . import db,SerializerMixin
from sqlalchemy.orm import validates

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__= 'restaurant_pizzas'

    serialize_rules = ('-restaurant.restaurant_pizzas', '-pizza.pizza_restaurants')

    id = db.Column(db.Integer, primary_key=True)
    price db.Column(db.Integer, nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    pizza = db.relationship('Pizza', back_populates='pizza_restaurants')
    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')

    @validates('price')
    def validate_price(self, key, value):
        if value < 1 or value > 30:
            raise ValueError("Price must be between 1 and 30")
        return value