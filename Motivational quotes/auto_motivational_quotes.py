import datetime as dt
import random
import smtplib as st
my_email= "sama29571@gmail.com"
my_password="gsmdsbqqawpdalyo"

time_rn=dt.datetime.now()
day=time_rn.weekday()
with open("quotes.txt") as file:
    quotes_list=file.readlines()
    quote=random.choice(quotes_list)
    print(quote)
if day == 1:
    with st.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,#sending email to myself
                            msg=f"Subject:Quote for the day \n\n {quote}")
