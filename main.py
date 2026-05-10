# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import os
import pandas as pd
import random
import smtplib
import datetime as dt
from pathlib import Path

my_email = "porivaldovidro@gmail.com"
password = "egkfojhwszqkmcfs"
birthdays_file = pd.read_csv('birthdays.csv')
birthdays = birthdays_file.to_dict('records')
now = dt.datetime.now()
for date in birthdays:
    if date['month'] == now.month and date['day'] == now.day:
        path = Path("./letter_templates")
        files = os.listdir(path)
        file_name = random.choice(files)
        with open(path / file_name, "r") as file:
            model = file.readlines()
            message = ""
            for line in model:
                if "[NAME]" in line:
                    line = line.replace("[NAME]", date['name'])
                message = message + line
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(user=my_email, password=password)
            smtp.sendmail(
                from_addr=my_email,
                to_addrs=date['email'],
                msg=f"Subject:Birthday wish\n\n{message}"
            )
