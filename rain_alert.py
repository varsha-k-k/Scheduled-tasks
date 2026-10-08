
import os
import requests
import smtplib

EMAIL = os.environ.get("MY_EMAIL")
PASSWD =os.environ.get("MY_PASSWORD")

API_KEY =os.environ.get("WEATHER_API")
MY_LAT =11.921349053933902
MY_LON=75.35472439934574

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
    msg = "Subject: Bring an umbrella!!\n\nIt will rain today buddy"
    with smtplib.SMTP("smtp.gmail.com" ,587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=EMAIL,
                            msg=msg)

