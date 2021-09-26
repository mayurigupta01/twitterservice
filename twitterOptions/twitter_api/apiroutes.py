import time

from flask import Blueprint, jsonify, render_template, request
import requests

twitter_api_blueprint = Blueprint("twitter_api", __name__, "url_prefix=/api/option")


@twitter_api_blueprint.route('/', methods=['GET'])
def landing_page():
    twitter_options = ['look_tweet', 'delete_tweet']
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


@twitter_api_blueprint.route('/update', methods=['PUT'])
def update_tweet():
    return {"message": "retweet tweet successfully"}


# Author- Mayuri
@twitter_api_blueprint.route('/delete', methods=['GET'])
def delete():
    # find the userid of the passed username
    from helper.readyaml import read_yaml
    my_dict = read_yaml()
    from twitterOptions.twitter_api.UserOnTwitter import get_userid
    user = get_userid(my_dict['credentials']['username'])
    userid = user['data']['id']

    # create a request to fetch tweets and return response on web page- build a request that contains userid field.
    my_headers = {'Authorization':
                      'Bearer {}'.format(my_dict['credentials']['token'])}



    #- get all the tweets of the user from cred.yaml
    response = requests.get(url="https://api.twitter.com/2/users/{}/tweets".format(userid), headers=my_headers)
    tweets = response.json()
    mytweetlist = tweets['data']
    tweet_id = []
    #add just tweet id in the list
    for tweet in mytweetlist:
        tweet_id.append(tweet['id'])
    print(tweet_id)
    #craete OAuth 1.0 context authorization
    my_headers = {"authorization": 'OAuth' +
                                   "oauth_consumer_key=Nt5n3NnTPppp14X0zhTBCDzgh," +
                                   "oauth_token=1437176256022253568-PN9skR05AWQ75tz4df6woUUhibEps7," +
                                   "oauth_signature_method=HMAC-SHA1," +
                                   "oauth_timestamp=1632691215," +
                                   "oauth_nonce=o67dPLC8uCW," +
                                   "oauth_version=1.0," +
                                   "oauth_signature=Jt0ANYP18nEdSen2Chdk6o1bOEQ%3D"
                  }
    response = requests.get(url="https://api.twitter.com/1.1/statuses/destroy/{}.json".format(tweet_id[0]), headers=my_headers)
    return response.json()

# Author-Mayuri
def error_message():
    payload = {'error': 400, "message": "Bad request", "possible error": "could be wrong username"}
    response = jsonify(payload)
    return response
