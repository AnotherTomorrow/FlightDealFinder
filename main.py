from flight_search import FlightSearch
from data_manager import DataManager

flight_search = FlightSearch()
data_updater = DataManager()
sheet_data = data_updater.get_destination_data()
length_sheet_data = len(sheet_data)

# For loop gets Iata code from kiwi and updates the spreadsheet. Uncomment if spreadsheet isn't made yet.
# for i in range(0, length_sheet_data):
#     if sheet_data[i]['iataCode'] == "":
#         response = flight_search.iata_code(sheet_data[i])
#         sheet_data[i] = response
#         data_updater.update_code(sheet_data[i])

for i in range(0, length_sheet_data):
    flight_search.find_deal(sheet_data[i])
