from flask import Blueprint, jsonify, make_response, request
from server.models import db
from server.models.restaurant_pizza import RestaurantPizza

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__, url_prefix='/restaurant_pizzas')

@restaurant_pizza_bp.route('/', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    try:
        new_rp = RestaurantPizza(
            price=data['price'],
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        db.session.add(new_rp)
        db.session.commit()
        return make_response(jsonify(new_rp.to_dict()), 201)
    except (KeyError, ValueError) as e:
        return make_response(jsonify({"errors": [str(e)]}), 400)