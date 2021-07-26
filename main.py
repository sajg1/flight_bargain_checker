#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from flight_search import FlightSearch
from data_manager import DataManager
from datetime import datetime, timedelta

data_manager = DataManager()
sheety_data = data_manager.get_destination_data()
flight_search = FlightSearch()

ORIGIN_CITY_IATA = "LON"
tomorrow = datetime.now() - timedelta(days=1)
six_months_date_from_today = datetime.now() + timedelta(days=(6*30))


for _ in sheety_data:
    if _['iataCode'] == "":
        flight_search = FlightSearch()
        _['iataCode'] = flight_search.get_destination_code(_['city'])

data_manager.destination_data = sheety_data
data_manager.update_iata_code()

for destination in sheety_data:
    flight_search.check_flight(
        city_of_origin=ORIGIN_CITY_IATA,
        destination_city=destination['iataCode'],
        date_from=tomorrow,
        date_to=six_months_date_from_today
    )
