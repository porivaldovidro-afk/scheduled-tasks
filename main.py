import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "916d3762b87147402f71f7010977b5a2"
MY_LAT = -8.839988
MY_LON = 13.289437
parameters = {
    'lat': MY_LAT,
    'lon': MY_LON,
    'appid': API_KEY,
    'cnt': 5
}

load_dotenv()
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()
weather = [item['weather'] for item in data['list']]
weather_id = [item[0]['id'] for item in weather]
will_rain = False
for id in weather_id:
    if id < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Vai chover hoje. Lembra-te de levar o guarda-chuva ☔.",
        from_="+17253021127",
        to="+244973892640",
    )
    print(message.status)
