from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

from .restaurant import Restaurant
from .pizza import Pizza
from .restaurant_pizza import RestaurantPizza