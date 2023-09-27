import requests
import datetime as dt
import smtplib as st
my_email= "sama29571@gmail.com"
my_password="gsmdsbqqawpdalyo"

#SUNSET AND SUNRISE
#THIS API reqs parameters
#to do this check docs and find out how it should be
#so you take the keys from the docs and place em in a dict
api_params={
    "lat": 54.555555 ,
    "long": -4.555555,
#optional 3rd parameter called formatted either 0 or1
#we turn it off so we can compare with current time
#so that we can alert user of sun rise and set
    "formatted":0,
}

response=requests.get(url="https://api.sunrise-sunset.org/json",params=api_params)
response.raise_for_status()#to raise an exception for any staus error
data= response.json()
#now this data will give you the sunrise.set of loaction you entered
print(data)
#this api gives plenty info like day length den tins
#but in this eg we only want the sunrise and sunset times
sunrise= data["results"]["sunrise"]
sunset= data["results"]["sunset"]
print(sunrise)
print(sunset)

sunrise_in_hrs=sunrise.split("T")[1].split(":")[0]
#so split it then take the index which contains the hour
print(sunrise_in_hrs)
sunset_in_hrs=sunset.split(":")[1]
print(sunset_in_hrs)
now=dt.datetime.now().time()
time_rn_hrs=now.hour

if time_rn_hrs==sunset_in_hrs or time_rn_hrs==sunrise_in_hrs :
    with st.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        if time_rn_hrs==sunset_in_hrs:
            connection.sendmail(from_addr=my_email, to_addrs=my_email,  # sending email to myself
                                msg=f"Subject:Quote for the day \n\n It is almost time for you to see the beautiful sunset")
        elif time_rn_hrs==sunrise_in_hrs:
            connection.sendmail(from_addr=my_email, to_addrs=my_email,  # sending email to myself
                                msg=f"Subject:Quote for the day \n\n It is almost time for you to see the beautiful sunrise")
