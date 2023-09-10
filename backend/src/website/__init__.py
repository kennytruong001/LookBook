from flask import Flask
from helper import getConfigs

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KET'] = 'akljsdnfkjansd'

    from routes import user_views, customer_views
    from routes import auth

    app.register_blueprint(user_views, url_prefix='/')
    app.register_blueprint(customer_views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app