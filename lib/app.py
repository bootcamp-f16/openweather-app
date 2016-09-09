import os
from lib.api import API

class App():
    def __init__(self, api_key):
        self.api_key = api_key
        self.api = API(api_key)

    def run(self):
        while True:
            try:
                print("Enter zip code")
                zip = input(">>> ")
                self.api.get_current_weather(zip=zip)
            except ValueError as e:
                print("Error getting the weather: {}".format(e))
