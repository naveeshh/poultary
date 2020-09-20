from flask import Flask
from flask_cors import CORS

from flask import jsonify
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from src.views.customers import cust

def create_app():
    """ provides flask app instance"""
    # flask app instantiation
    app = Flask(__name__)

    # cross origin resource sharing
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/poultry"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    db.init_app(app)

    from src.views.orders import orders
    app.register_blueprint(orders)

    app.add_url_rule("/customers", methods=['GET'], view_func=cust)

    # Swagger setup
    swaggerui_blueprint = get_swaggerui_blueprint("/swagger", "http://localhost:1234/spec")
    app.register_blueprint(swaggerui_blueprint, url_prefix="/swagger")

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "My Poultry API"
        return jsonify(swag)

    return app



