import os
import requests
def print_message():
    print("This is capfd() method test")


def get_config_value(key):
    return os.environ.get(key, None)

def fetch_data_from_api(url):
    response = requests.get(url)
    return response.json()
