# Author-Mayuri

import requests
from helper.readyaml import read_yaml


def get_userid(username):
    my_dict = read_yaml()
    my_headers = {'Authorization':
                      'Bearer {}'.format(my_dict['credentials']['token'])}
    response = requests.get(url="https://api.twitter.com/2/users/by/username/{}".format(username), headers=my_headers)
    print(response)
    if response.status_code == 200:
        print("The request was a success!")
        user = response.json()
        return user
    else:
        print("Result not found!")
        return False
