# Author-Mayuri

from flask import Flask


def create_app():
    app = Flask(__name__)
    with app.app_context():
        from .twitter_api.apiroutes import twitter_api_blueprint
        app.register_blueprint(twitter_api_blueprint)
        return app
