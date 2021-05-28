#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
import requests

SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
SHEETY_AUTH = os.environ.get("AUTH_HEADER")
sheety_endpoint = f"https://api.sheety.co/{SHEETY_USERNAME}/flightdealstracker/prices"

sheety_headers = {
    "Authorization": SHEETY_AUTH
}

response = requests.get(url=sheety_endpoint, headers=sheety_headers)
print(response.textd)
