from flask import Flask
from flask_migrate import Migrate 
from models import db
from controllers.restaurant_controller import restaurant_bp
from controllers.pizza_controller import pizza_bp
from controllers.restaurant_pizza_controller import restaurant_pizza_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'

migrate = Migrate(app,db)
db.init_app(app)

app.register_blueprint(restaurant_bp)
app.register_blueprint(pizza_bp)
app.register_blueprint(restaurant_pizza_bp)

@app.route("/")
def index():
    return "🍕 Restaurant API is running!"

if __name__=='__main__':
    app.run(debug=True, port=5555)