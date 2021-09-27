import json
from time import sleep

from flask import Blueprint, jsonify, render_template,redirect, url_for
from helper.readyaml import read_yaml
import requests
from werkzeug.http import HTTP_STATUS_CODES

twitter_api_blueprint = Blueprint("twitter_api", __name__, "url_prefix=/api/option")


@twitter_api_blueprint.route('/', methods=['GET'])
def landing_page():
    return render_template('homepage.html')


# Author-Mayuri(implement lookup tweets )
@twitter_api_blueprint.route('/looktweet/<username>', methods=['GET'])
def lookup_tweet(username):
    # find the userid of the passed username
    try:
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
        tweet_text = []
        for tweet in mytweetlist:
            tweet_text.append(tweet['text'])
        return render_template('tweetlookup.html', tweet_text=tweet_text, username=username)

    except:
        response = error_message()
        return response


@twitter_api_blueprint.route('/twitter_tweets', methods=['GET'])
def get_tweets():
    my_dict = read_yaml()
    my_headers = {'Authorization':
                          'Bearer {}'.format(my_dict['credentials']['token'])}
    response = requests.get(url="https://api.twitter.com/2/users/{}/tweets".format(my_dict['credentials']['user_id']),headers=my_headers)
    if response.ok:
        results = response.json()
        return render_template('tweethiding.html',tweets = results, success = "failure")
    else:
        return response.raise_for_status();

@twitter_api_blueprint.route('/hide_tweet/<tweetid>', methods=['GET'])
def hide_tweet(tweetid):
    my_dict = read_yaml()
    print(tweetid,my_dict)
    my_headers = {'Authorization': 'OAuth oauth_consumer_key="{}",oauth_token="{}",oauth_signature_method="HMAC-SHA1",oauth_nonce="65FB5akRnAK",oauth_version="1.0",oauth_signature="maLA%2FHVv5gSofBKPQmef72JvXGg%3D"'.format(mydict['credentials']['oauth1_consumer_key'],mydict['credentials']['oauth1_access_token']),
  'Content-Type': 'application/json'}
    response = requests.put(url="https://api.twitter.com/2/tweets/{}/hidden".format(tweetid), headers=my_headers,json={"hidden":"true"})
    response =
    return redirect('/twitter_tweets',success = "success")


@twitter_api_blueprint.route('/delete', methods=['DELETE'])
def delete():
    return {"message": "Delete Re-tweet successfully"}


# Author-Mayuri
def error_message():
    payload = {'error': 400, "message": "Bad request", "possible error": "could be wrong username"}
    response = jsonify(payload)
    return response
