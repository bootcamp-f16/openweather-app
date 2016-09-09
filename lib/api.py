import requests
class API():
    def __init__(self, api_key):
        self.api_key = api_key
        self.requests = requests
        self.base_url = "http://api.openweathermap.org/data/2.5"
    def get_base_payload(self):
        return {
            'appid': self.api_key,
        }

    def get_current_weather(self, zip=""):
        if not zip.isdigit() and len(zip) != 5:
            raise ValueError("5 digit zipcode is required")

        payload = self.get_base_payload()
        url = "{}{}".format(self.base_url, "/weather")
        payload["zip"] = "{},us".format(zip)
        r = requests.get(url, params=payload)

        return r.json()