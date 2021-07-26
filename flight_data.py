class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, departure_city, departure_airport, destination_city, destination_airport, departure_date, return_date):
        self.price = price
        self.departure_city = departure_city
        self.departure_airport = departure_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.departure_date = departure_date
        self.return_date = return_date
