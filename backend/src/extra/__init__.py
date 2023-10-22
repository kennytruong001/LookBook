from flask import Flask, render_template, request
from . import config as secret
import boto3 


def create_app() -> Flask:
    """Initialize Flask App

    Returns:
        Flask: initialized app
    """
    app = Flask(__name__)

    db = boto3.resource('dynamodb',
                    aws_access_key_id=secret["ACCESS_KEY_ID"],
                    aws_secret_access_key=secret["ACCESS_SECRET_KEY"],
                    aws_session_token=secret["AWS_SESSION_TOKEN"])
    
    client = boto3.client('dynamodb')
    table = boto3.resource('dynamodb', aws_access_key_id=secret["ACCESS_KEY_ID"],
                     aws_secret_access_key=secret["ACCESS_SECRET_KEY"]).Table("LookBook_Database")

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app