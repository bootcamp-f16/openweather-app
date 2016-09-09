

class Weather():
    def __init__(self, base_data):
        self.base_data = base_data

    def display_weather(self):
        base_data = self.base_data
        print(base_data)
        temperature = base_data["main"]["temp"]
        print("")
        print("Curret Conditions: {}".format(base_data["weather"][0]["main"]))
        print("Description: {}".format(base_data["weather"][0]["description"]))
        print("Current Temperature: {}".format(temperature))
        print("")