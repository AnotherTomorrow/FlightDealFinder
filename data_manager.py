import requests


class DataManager:

    # Updates the sheety Excel sheet using API
    def get_destination_data(self):
        self.sheety_endpoint = "https://api.sheety.co/a0abcb9275b4af8eb3d89a8a68a3ff9f/flightDeals/prices"
        sheety_response = requests.get(url=self.sheety_endpoint)
        sheety_response.raise_for_status()
        self.destination_data = sheety_response.json()["prices"]
        return self.destination_data

    def update_code(self, city_dict):
        row_id = city_dict['id']
        row_code = city_dict['iataCode']
        sheety_update = f"{self.sheety_endpoint}/{row_id}"
        update_params = {
            "price": {
                "iataCode": row_code
            }
        }

        update_row = requests.put(sheety_update, json=update_params)
        update_row.raise_for_status()
