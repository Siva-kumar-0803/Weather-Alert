import requests
from twilio.rest import Client

account_sid = ' give twillo id'
auth_token = 'give twilio token'
client = Client(account_sid, auth_token)

key = "give your openweathermap authentication key"
source = "https://api.openweathermap.org/data/2.5/forecast"

parameter = {
    "lat": 39.768402,
    "lon": -86.158066,
    "appid": key,
    "cnt": 4
}
i = 5
response = requests.get(url=source, params=parameter)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    message = client.messages.create(
        body="Be alert bring an umbrella.",
        from_='twilio generated phone number',
        to='give your verified phone number'
    )
    print(message.sid)



