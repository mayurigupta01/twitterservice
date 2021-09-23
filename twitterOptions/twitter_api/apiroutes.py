from flask import Blueprint

twitter_api_blueprint = Blueprint("twitter_api", __name__, "url_prefix=/api/option")


@twitter_api_blueprint.route('/search', methods=['GET'])
def search_tweet():
    return {"message": "searched tweet successfully"}


# Author- Mayuri (implement post tweet)

@twitter_api_blueprint.route('/create', methods=['POST'])
def post_tweet():
    return {"message": "created tweet successfully"}


@twitter_api_blueprint.route('/update', methods=['PUT'])
def update_tweet():
    return {"message": "retweet tweet successfully"}


@twitter_api_blueprint.route('/delete', methods=['DELETE'])
def delete():
    return {"message": "Delete Re-tweet successfully"}
