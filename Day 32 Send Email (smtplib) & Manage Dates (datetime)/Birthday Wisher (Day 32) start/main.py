"""
Email SMTP and the datetime module
Email SMTP(Simple Mail Transfer Protocol) -> email by python
"""
#Monday Motivation Project
import smtplib
import datetime as dt
import random

MY_EMAIL = "appbreweryinfo@gmail.com"
MY_PASSWORD = "abcd1234()"

now = dt.datetime.now()
weekday = now.weekday()
print(weekday)
if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs='smbb1693@gmail.com',
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )

# import smtplib
#
# my_email = '646546@you-spam.com'
# password = '123456'
#
# with smtplib.SMTP('amtp.you-spam.com') as connection:
#     connection.starttls()  # tls(transprot layer security) -> make connection secure
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs='someemail@gmail.com',
#         msg='Subject:Yo\n\nThis is body'
#     )

## Working with date and time in Python
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)