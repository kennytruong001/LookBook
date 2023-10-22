from flask import Flask


def create_app():
    app = Flask(__name__)
    #app.config['SECRET_KET'] = 'akljsdnfkjansd'

    from .routes.user_views import user_views
    #from .route.customer_views import customer_views
    from .routes.auth import auth

    app.register_blueprint(user_views, url_prefix='/')
    #app.register_blueprint(customer_views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app