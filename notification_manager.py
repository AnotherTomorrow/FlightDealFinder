from twilio.rest import Client

account_sid = "YOUR TWILIO SID"
auth_token = "YOUR TWILIO AUTH TOKEN"


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
