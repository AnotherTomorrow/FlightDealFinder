import requests
import datetime as dt

from notification_manager import NotificationManager

notify = NotificationManager()

KIWI_ID = "YOUR KIWI ID"
KIWI_API_KEY = "YOUR KIWI API KEY"

# Headers to pass
KIWI_HEADER = {
    "Content-Type": "application/json",
    "apikey": KIWI_API_KEY
}

KIWI_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
FLIGHT_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"

six_months = dt.datetime.now() + dt.timedelta(days=6*30)
today = dt.datetime.now()


class FlightSearch:

    # Receives Iata code from the travelling website API
    def iata_code(self, city_dict):
        city = city_dict['city']

        kiwi_params = {
            "term": city
        }

        request = requests.get(url=KIWI_ENDPOINT, params=kiwi_params, headers=KIWI_HEADER)
        request.raise_for_status()
        response = request.json()
        city_search = response['locations'][0]['name']

        if city == city_search:
            city_dict['iataCode'] = response['locations'][0]['code']

        return city_dict

    # Finds deal that fits criteria and passes all information to sms notification.
    def find_deal(self, airport):
        flight_params = {
            "fly_from": "LON",
            "fly_to": airport["iataCode"],
            "date_from": today.strftime("%d/%m/%Y"),
            "date_to": six_months.strftime("%d/%m/%Y"),
            "curr": "GBP",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "limit": 1
        }

        request = requests.get(url=FLIGHT_SEARCH_ENDPOINT, params=flight_params, headers=KIWI_HEADER)
        request.raise_for_status()

        try:
            response = request.json()['data'][0]
        except IndexError:
            print(f"No flights found for {airport['city']}")
            return None

        flight_price = response['price']
        nights_out = response['nightsInDest']
        departure = response['route'][-1]['local_departure'].split("T")[0]
        arrival = response['route'][0]['local_arrival'].split("T")[0]

        if airport['lowestPrice'] > flight_price:
            notify.send_text(airport=airport, flight_price=flight_price, nights=nights_out, arrival=arrival, departure=departure)
