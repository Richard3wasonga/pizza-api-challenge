from . import db, SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

class Pizza(db.Model, SerializerMixin):
    __tablename__= 'pizzas'

    serialize_rules = ('-pizza_restaurants.pizza',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String, nullable=False)
    pizza_restaurants = db.relationship('RestaurantPizza', back_populates='pizza')
    restaurants = association_proxy('pizza_restaurants', 'restaurant')