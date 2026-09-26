
import datetime as dt
import pandas as pd
import random
import smtplib
import os

EMAIL = os.environ.get("MY_EMAIL")
PASSWD = os.environ.get("MY_PASSWD")

noww = dt.datetime.now()
today = (noww.month , noww.date)
df = pd.read_csv('birthdays.csv')
newdict = {(row.month ,row.day) : row  for (index , row) in df.iterrows()}
# print(newdict)

if today in newdict:
    random_no = random.randint(1 ,3)
    person = newdict[today]
    with open(f"letter_templates/letter_{random_no}.txt" , "r") as letter :
        contents = letter.read()
        replaced = contents.replace("[NAME]" ,person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWD)
        connection.sendmail(from_addr=EMAIL,
                                to_addrs=person["email"],
                                msg=f"Subject:Happy Birthday \n\n{replaced}")



