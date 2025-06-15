from . import db, SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

class Restaurant(db.Model, SerializerMixin):
    __tablename__= 'restaurants'

    serialize_rules = ('-restaurant_pizzas.restaurant',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address =db.Column(db.String, nullable=False)
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant', cascade='all, delete')
    pizzas = association_proxy('restaurant_pizzas', 'pizza', creator=lambda pizza: RestaurantPizza(pizza=pizza) )

    def __repr__(self):
        return f"<Restaurant id={self.id} name='{self.name} address={self.address}'>"