from flask import Blueprint, jsonify, make_response
from models import db
from models.pizza import Pizza

pizza_bp = Blueprint('pizza_bp', __name__, url_prefix='/pizzas')

@pizza_bp.route('/', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return make_response(jsonify([pizza.to_dict() for pizza in pizzas]), 200)