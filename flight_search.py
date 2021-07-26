import requests
import os
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")


class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        result = response.json()
        iataCode = result['locations'][0]['code']
        return iataCode

    def check_flight(self, city_of_origin, destination_city, date_from, date_to):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": city_of_origin,
            "fly_to": destination_city,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=headers, params=query )

        try:
            data = response.json()
            print(data)

        except IndexError:
            print(f"No flights found for {destination_city}.")
            return None


