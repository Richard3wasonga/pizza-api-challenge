from flask import Blueprint, jsonify, make_response, request
from server.models import db
from server.models.restaurant import Restaurant

restaurant_bp = Blueprint('restaurant_bp', __name__, url_prefix='/restaurants')

@restaurant_bp.route('/', methods=['GET'])
def get_restaurants():
    restaurants = db.session.query(Restaurant).all()
    return make_response(jsonify([r.to_dict() for r in restaurants]), 200)

@restaurant_bp.route('/<int:id>', methods=['GET', 'DELETE'])
def handle_restaurant(id):
    restaurant = db.session.get(Restaurant, id)

    if not restaurant:
        return make_response(jsonify({"error": "Restaurant not found"}), 404)

    if request.method == 'GET':
        return make_response(jsonify(restaurant.to_dict()), 200)

    elif request.method == 'DELETE':
        db.session.delete(restaurant)
        db.session.commit()
        return make_response('', 204)