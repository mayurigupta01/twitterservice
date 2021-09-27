import unittest
import requests
import logging

# test cases for all the twitter options

api_base_url = "http://127.0.0.1:5000/"

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
req_log = logging.getLogger('requests.packages.urllib3')
req_log.setLevel(logging.DEBUG)
req_log.propagate = True


class TestStringMethods(unittest.TestCase):

    def test_tweet_lookup_1(self):
        response = requests.get(api_base_url + "looktweet?username=justinbieber")
        self.assertEqual(response.status_code, 200)

    def test_tweet_lookup_2(self):
        response = requests.get(api_base_url + "looktweet?username=elonmusk")
        self.assertEqual(response.status_code, 200)

    def test_tweet_lookup_3(self):
        response = requests.get(api_base_url + "looktweet?username=Katyperry")
        self.assertEqual(response.status_code, 200)

    def test_user_follower1(self):
        response = requests.get(api_base_url + "followers?username=rihanna")
        self.assertEqual(response.status_code, 200)

    def test_user_follower2(self):
        response = requests.get(api_base_url + "followers?username=BrunoMars")
        self.assertEqual(response.status_code, 200)
    
    def test_find_tweets(self):
        response = requests.get(api_base_url + "twitter_tweets")
        self.assertEqual(response.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()
