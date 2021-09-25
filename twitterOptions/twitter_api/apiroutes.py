import json
from time import sleep

from flask import Blueprint, jsonify, render_template
import requests
from werkzeug.http import HTTP_STATUS_CODES

import os

twitter_api_blueprint = Blueprint("twitter_api", __name__, "url_prefix=/api/option")


@twitter_api_blueprint.route('/', methods=['GET'])
def landing_page():
    return render_template('Welcome to twitter functions')


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
    mytweetlist = tweets['data']
    tweet_dict = {}
    tweet_text = []
    counter = 1
    for tweet in mytweetlist:
        # tweet_dict[counter] = tweet['text']
        tweet_text.append(tweet['text'])
        print(tweet_text)
        # counter = counter + 1
    # print(tweet_dict)
    # data_json = json.dumps(tweet_dict, indent=6)
    # response = jsonify({'results': tweet_text})
    return render_template('tweetlookup.html', tweet_text=tweet_text, username=username)


@twitter_api_blueprint.route('/update', methods=['PUT'])
def update_tweet():
    return {"message": "retweet tweet successfully"}

# Author-Pratiksha


@twitter_api_blueprint.route('/delete', methods=['DELETE'])
def delete_tweet(tweetId, username):
    from helper.readyaml import read_yaml
    my_dict = read_yaml()
    from twitterOptions.twitter_api.UserOnTwitter import get_userid
    user = get_userid(username)
    userid = user['data']['id']

    # create a request to fetch tweets and return response on web page- build a request that contains userid field.
    my_headers = {'Authorization':
                      'Bearer {}'.format(my_dict['credentials']['token'])}

    response = requests.request(method="DELETE", url="https://api.twitter.com/2/users/{}".format(tweetId),
                                headers=my_headers)
    print(response.status_code)
    if response.status_code == 401:
        return False
    return {"message": "Delete ReTweet Successfully"}


# Author-Mayuri
def error_message(status_code, message):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    response = jsonify(payload)
    response.status_code = status_code
    return response
