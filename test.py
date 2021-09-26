import unittest
import requests

# test cases for all the twitter options

api_base_url = "http://127.0.0.1:5000/"


class TestStringMethods(unittest.TestCase):

    def test_tweet_lookup_1(self):
        response = requests.get(api_base_url + "looktweet/justinbieber")
        self.assertEqual(response.status_code, 200)

    def test_tweet_lookup_2(self):
        response = requests.get(api_base_url + "looktweet/BrunoMars")
        self.assertEqual(response.status_code, 200)

    def test_tweet_lookup_3(self):
        response = requests.get(api_base_url + "looktweet/Katyperry")
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
