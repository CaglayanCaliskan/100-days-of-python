import pandas
import random
import datetime as dt
import smtplib


now = dt.datetime.now()
print(now.weekday())

my_email = "caliskancaglayan@gmail.com"
password = "vnpbiwqrekzbcpdi"

if now.weekday() == 4:
    with open('./quotes.txt') as quotes:
        data = quotes.readlines()
        quot = random.choice(data)

    print(quot)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="caosfreeman@gmail.com",
            msg=f"Subject:Güzel Sözler Köşesi\n\n{quot}".encode("utf8")
        )
