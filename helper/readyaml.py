# Author-Mayuri
import yaml
import os


def read_yaml():
    yamlpath = os.getcwd()
    my_dict = {}
    with open(yamlpath + "/twitterOptions/static/creds.yaml", "r") as stream:
        try:
            my_dict = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return my_dict


