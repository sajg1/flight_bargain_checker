#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from flight_search import FlightSearch
from data_manager import DataManager

data_manager = DataManager()
sheety_data = data_manager.get_destination_data()


for _ in sheety_data:
    if _['iataCode'] == "":
        flight_search = FlightSearch(_['city'])
        _['iataCode'] = flight_search.get_destination_iataCode()

data_manager.destination_data = sheety_data
data_manager.update_iata_code()

print(sheety_data)
