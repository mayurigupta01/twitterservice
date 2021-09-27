import time

import json
import requests
from flask import Blueprint, jsonify, render_template, request
from requests_oauthlib import OAuth1

twitter_api_blueprint = Blueprint("twitter_api", __name__, "url_prefix=/api/option")


@twitter_api_blueprint.route('/', methods=['GET'])
def landing_page():
    twitter_options = ['tweet_lookUp', 'most_recent_tweet', 'find_followers', 'create_tweet']
    return render_template('homepage.html', twitter_options=twitter_options)


# Author-Mayuri(implement lookup tweets )
@twitter_api_blueprint.route('/looktweet', methods=['GET'])
def lookup_tweet():
    # fetch the username from the form
    username = request.args.get('username')
    # find the userid of the passed username
    try:
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
        tweet_text = []
        for tweet in mytweetlist:
            tweet_text.append(tweet['text'])
            time.sleep(1)
        return render_template('tweetlookup.html', tweet_text=tweet_text, username=username)

    except:
        response = error_message()
        return response


# Author - Martin Duong
@twitter_api_blueprint.route('/mostRecentTweet', methods=['GET'])
def mostRecentTweet():
    # Fetch and build query
    query = request.args.get('query')
    newQuery = "?query=" + query + " -is:retweet"

    try:
        from helper.readyaml import read_yaml
        my_dict = read_yaml()

        auth = {"Authorization": "Bearer {}".format(my_dict['credentials']['token'])}
        url = "https://api.twitter.com/2/tweets/search/recent{}".format(newQuery)

        response = requests.request("GET", url, headers=auth)

        # Convert from JSON object to JSON string to Python Dictionary
        tweets = json.loads(json.dumps(response.json()))

        # Checks if no tweets are found from user search
        if (response.status_code == 200 and response.text == "{\"meta\":{\"result_count\":0}}"):
            return render_template('mostRecentTweet.html', recentTweet="No Tweets Found", query=query)

        # Returns the most recent tweet from user search
        recentTweet = tweets["data"][0]["text"]
        return render_template('mostRecentTweet.html', recentTweet=recentTweet, query=query)
    except:
        response = recentTweetError(response.status_code, response.text)
        return response


@twitter_api_blueprint.route('/update', methods=['PUT'])
def update_tweet():
    return {"message": "retweet tweet successfully"}


# Author- Mayuri & Pratiksha
@twitter_api_blueprint.route('/followers', methods=['GET'])
def find_followers():
    username = request.args.get('username')
    # find the userid of the passed username
    from helper.readyaml import read_yaml
    my_dict = read_yaml()
    from twitterOptions.twitter_api.UserOnTwitter import get_userid
    user = get_userid(username)
    userid = user['data']['id']

    # create a request to fetch tweets and return response on web page- build a request that contains userid field.
    my_headers = {'Authorization':
                      'Bearer {}'.format(my_dict['credentials']['token'])}

    # - get all the tweets of the user from cred.yaml
    response = requests.get(url="https://api.twitter.com/2/users/{}/followers".format(userid), headers=my_headers)
    tweets = response.json()
    mytweetlist = tweets['data']
    follower_name = []
    # add just follower name in the list
    for tweet in mytweetlist:
        follower_name.append(tweet['name'])
    print(follower_name)
    return render_template('userfollowers.html', follower_name=follower_name, username=username)


# Author- Mayuri
@twitter_api_blueprint.route('/createtweet', methods=['POST'])
def create_tweet():
    text = request.form['tweet']
    from helper.readyaml import read_yaml
    my_dict = read_yaml()
    # create a request to post tweets and return response on web page that tweet is successfully created.

    auth_session = OAuth1(my_dict['credentials']['consumerkey'], my_dict['credentials']['consumersecret'],
                          my_dict['credentials']['accesstoken'],
                          my_dict['credentials']['tokensecret'])
    response = requests.post(url="https://api.twitter.com/1.1/statuses/update.json?status={}".format(text),
                             auth=auth_session)
    return response.json()


# Author-Mayuri
def error_message():
    payload = {'error': 400, "message": "Bad request", "possible error": "could be wrong username"}
    response = jsonify(payload)
    return response


# Author - Martin Duong
def recentTweetError(responseCode, responseText):
    payload = {'error': responseCode, "message": responseText}
    response = jsonify(payload)
    return response
