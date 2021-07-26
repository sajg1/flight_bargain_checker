import os
import requests
from pprint import pprint

SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
SHEETY_AUTH = os.environ.get("AUTH_HEADER")
sheety_endpoint = f"https://api.sheety.co/{SHEETY_USERNAME}/flightdealstracker/prices"

sheety_headers = {
    "Authorization": SHEETY_AUTH
}


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=sheety_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(self.destination_data)
        return self.destination_data

    def update_iata_code(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{sheety_endpoint}/{city['id']}", json=new_data)
            # print(response.text)