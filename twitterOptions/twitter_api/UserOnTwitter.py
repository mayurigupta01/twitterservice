# app/twitter_api/api/UserOnTwitter.py
import requests


class UserOnTwitter:
    @staticmethod
    def get_user(bearer_token, userid):
        headers = {
            'Authorization': "Bearer".format(bearer_token)
        }
        response = requests.request(method="GET", url="https://api.twitter.com/2/users/{}".format(userid),
                                    headers=headers)
        if response.status_code == 401:
            return False
        user = response.json()
        return user
