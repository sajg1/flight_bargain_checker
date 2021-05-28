#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
import requests
from flight_search import FlightSearch
from pprint import pprint

SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
SHEETY_AUTH = os.environ.get("AUTH_HEADER")
sheety_endpoint = f"https://api.sheety.co/{SHEETY_USERNAME}/flightdealstracker/prices"

sheety_headers = {
    "Authorization": SHEETY_AUTH
}

response = requests.get(url=sheety_endpoint, headers=sheety_headers)
sheet_data = response.json()['prices']
# pprint(sheet_data)
for _ in sheet_data:
    if _['iataCode'] == "":
        flight_search = FlightSearch(_['city'])
        _['iataCode'] = flight_search.search_iataCode()

