from flask import Blueprint


twitter_api_blueprint = Blueprint("twitter_api", __name__, "url_prefix=/api/option")

@twitter_api_blueprint.route('/', methods=['GET'])
def landing_page():
    return "Welcome to HomePage"



#Author-Mayuri
@twitter_api_blueprint.route('/looktweet', methods=['GET'])
def search_tweet():

    #find the userid of the passed username
    from helper.readyaml import read_yaml
    my_dict = read_yaml()
    from twitterOptions.twitter_api.UserOnTwitter import get_userid
    user = get_userid('elonmusk')
    userid= user['data']['id']

    #craete a request to fetch tweets and return response on web page


    return {"message": "searched tweet successfully",
            "tokens":  my_dict['credentials']['token']
            }


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
