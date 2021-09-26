from flask import Blueprint, jsonify, render_template, request
import requests

twitter_api_blueprint = Blueprint("twitter_api", __name__, "url_prefix=/api/option")



@twitter_api_blueprint.route('/', methods=['GET'])
def landing_page():
    # username = request.form["username"]
    return render_template('homepage.html')


# Author-Mayuri(implement lookup tweets )
@twitter_api_blueprint.route('/looktweet', methods=['GET'])
def lookup_tweet():
    #fetch the username from the form
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
        return render_template('tweetlookup.html', tweet_text=tweet_text, username=username)

    except:
        response = error_message()
        return response


@twitter_api_blueprint.route('/update', methods=['PUT'])
def update_tweet():


    return {"message": "retweet tweet successfully"}


@twitter_api_blueprint.route('/delete', methods=['DELETE'])
def delete():
    return {"message": "Delete Re-tweet successfully"}


# Author-Mayuri
def error_message():
    payload = {'error': 400, "message": "Bad request", "possible error": "could be wrong username"}
    response = jsonify(payload)
    return response
