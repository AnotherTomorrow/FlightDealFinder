from twilio.rest import Client

account_sid = "ACa2da0a7277121d3a7e7bbc50501c5dab"
auth_token = "0603f500286267182d6e7e5efd5c309b"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_text(self, airport, flight_price, nights, arrival, departure):
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"Cheap Flight found.\nTo: {airport['city']}\nReturning: {departure} | Arriving: {arrival}\nTrip "
                 f"Length: {nights} days\nPrice: £{flight_price}",
            from_='+12517650560',
            to='3059173838'
        )
