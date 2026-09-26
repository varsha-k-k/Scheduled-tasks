# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import datetime as dt
import pandas as pd
import random
import smtplib

EMAIL = "codingpracticee56@gmail.com"
PASSWD = "fjru yyxp ydky klkh"

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



