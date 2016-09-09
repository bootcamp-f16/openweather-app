import os
from lib.api import API
from lib.weather import Weather

class App():
    def __init__(self, api_key):
        self.api_key = api_key
        self.api = API(api_key)

    def run(self):
        while True:
            try:
                print("Enter the name of a city.")
                location = input(">>> ")
                weather = Weather(self.api.get_current_weather(location=location))
                weather.display_weather()

            except ValueError as e:
                print("Error getting the weather: {}".format(e))
            except KeyError as e:
                print("There was an error reading the weather data at the location you entered.")