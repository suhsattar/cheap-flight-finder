#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from pprint import pprint
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()




