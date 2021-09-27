import http
import logging

import requests
from requests_oauthlib import OAuth1

http.client.HTTPConnection.debuglevel = 1

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

twitter_oauth = {
    "consumer_key": "Nt5n3NnTPppp14X0zhTBCDzgh",
    "consumer_secret": "pO9dzAxVkWwXv1gmRF6ab2pzc3O8gsacXRTfj42ctuApXsNcpq",
    "token": "1437176256022253568-PN9skR05AWQ75tz4df6woUUhibEps7",
    "token_secret": "yzNGz73qWqqFOZ6dlj2qHxogpfkGIuaJHZeJfYq9oTCOX",
}

sho = OAuth1(twitter_oauth["consumer_key"],twitter_oauth["consumer_secret"],twitter_oauth["token"],twitter_oauth["token_secret"])

response = requests.post(url="https://api.twitter.com/1.1/statuses/update.json?status=tweets upon tweet",
                        auth=sho)

print(response)
