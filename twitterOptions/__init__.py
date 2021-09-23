from flask import Flask
from twitterOptions.twitter_api import apiroutes


def create_app():
    app = Flask(__name__)
    with app.app_context():
        app.register_blueprint(apiroutes)
        return app
