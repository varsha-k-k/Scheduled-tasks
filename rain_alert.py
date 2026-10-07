# make a call to 5 days forecast api
import os
import requests
from twilio.rest import Client

import smtplib

EMAIL = MY_EMAIL
PASSWD =MY_PASSWORD

API_KEY =WEATHER_API
MY_LAT =11.921349053933902
MY_LON=75.35472439934574
# client = Client(TWILIO_APIKEY , TWILIO_CLIENTSECRET ,TWILIO_ACCSID)

para = {"lat" :MY_LAT,
        "lon":MY_LON,
        "appid":API_KEY,
        "cnt":4,}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast" , params=para)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"])
will_rain = False
for hour_data in weather_data["list"]:
    # for val in hour_data["weather"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:
    print("success")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs="codingpracticee56@gmail.com",
                            msg=f"Subject:Bring an umbrella!! \n\n It will rain today buddy")

