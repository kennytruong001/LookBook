from flask import Flask
from pymongo import MongoClient

from . import constants 


class Mongo: 
    """Mongo Client Connection.

    Set up like a Flask Extension. Uses app config when initialized with an app.
    """


    # def __init__(self, app=None):
    #     """Constructor for Mongo Client.

    #     Note that passing a flask app into the constructor is not recommended when using 
    #     Application Factory. See: https://flask.palletsprojects.com/en/2.2.x/patterns/appfactories/

    #     Args:
    #         app (_type_, optional): Flask App. Defaults to None.
    #     """
    #     self.client = None
    #     self.database = None
    #     self.user_collection = None

    #     if app is not None:
    #         self.init_app(app)


    def __init__(self, app=Flask): 
        """Initializes Mongo Client with a Flask app.

        Establishes a connection to MongoDB through the Flask App's config.
        This strategy is inline with the Flask Application Factory pattern.

        Args:
            app (_type_): Flask app
        """
        self.client = MongoClient(constants.CONNECTION_STRING)
        # self.client = MongoClient(
        #     host=app.config.get(constants["APP_KEY_MONGO_URI"]),
        #     port=app.config.get(constants["APP_KEY_MONGO_PORT"]),
        #     maxPoolSize=constants["MONGO_THREADS"]
        # )
        
        #self.database = self.client.get_database(constants.MONGO_DATABASE)
        self.database = self.client[constants.MONGO_DATABASE]
        self.user_collection = self.database[constants.USER_COLLECTION]