from flask import Flask
from configparser import ConfigParser, ExtendedInterpolation

from . import constants
from .routes import button_bp
#from .extensions import mongo, button_dao


def create_app() -> Flask:
    """Initialize Flask App

    Returns:
        Flask: initialized app
    """
    app = Flask(__name__, instance_relative_config=True)

    # initialize secrets from config.ini
    secrets = ConfigParser(interpolation=ExtendedInterpolation())
    secrets.read(constants.CONFIG_INI_PATH)

    # initialize config in flask app
    app.config[constants.APP_KEY_MONGO_URI] = secrets.get('MONGO_SETTINGS', 'uri')
    app.config[constants.APP_KEY_MONGO_PORT] = secrets.getint('MONGO_SETTINGS', 'port')

    # initialize flask extensions
    mongo.init_app(app)
    button_dao.init_app(app, mongo)

    # register blueprints
    app.register_blueprint(button_bp)

    return app