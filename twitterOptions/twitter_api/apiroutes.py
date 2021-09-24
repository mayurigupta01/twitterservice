import json
from flask import Blueprint, jsonify
import requests
from werkzeug.http import HTTP_STATUS_CODES

twitter_api_blueprint = Blueprint("twitter_api", __name__, "url_prefix=/api/option")


@twitter_api_blueprint.route('/', methods=['GET'])
def landing_page():
    return "Welcome to HomePage"


# Author-Mayuri(implement lookup tweets )
@twitter_api_blueprint.route('/looktweet/<username>', methods=['GET'])
def lookup_tweet(username):
    # find the userid of the passed username

    from helper.readyaml import read_yaml
    my_dict = read_yaml()
    from twitterOptions.twitter_api.UserOnTwitter import get_userid
    user = get_userid(username)
    userid = user['data']['id']

    # create a request to fetch tweets and return response on web page- build a request that contains userid field.
    my_headers = {'Authorization':
                      'Bearer {}'.format(my_dict['credentials']['token'])}

    response = requests.get(url="https://api.twitter.com/2/users/{}/tweets".format(userid), headers=my_headers)
    tweets = response.json()
    mytweetlist = tweets["data"]
    tweet_dict = {}
    counter = 1
    for tweet in mytweetlist:
        tweet_dict[counter] = tweet['text']
        counter = counter + 1
    return json.dumps(tweet_dict, indent=4)





@twitter_api_blueprint.route('/update', methods=['PUT'])
def update_tweet():
    return {"message": "retweet tweet successfully"}


@twitter_api_blueprint.route('/delete', methods=['DELETE'])
def delete():
    return {"message": "Delete Re-tweet successfully"}


# Author-Mayuri
def error_message(status_code, message):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    response = jsonify(payload)
    response.status_code = status_code
    return response
