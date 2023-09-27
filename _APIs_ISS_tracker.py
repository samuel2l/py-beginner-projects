# import requests
#ISS TRACKER FOR LOCATION OF SOME SATELLITE
#make a get request with url being the endpoint
# response= requests.get(url="http://api.open-notify.org/iss-now.json")
#printing this line alone gives <Response [200]>. The 200 reps the response code
#print(response)
#print(response.status_code)
#response.raise_for_status()

#to get the actual data we use the json func of the request
# data=response.json()
#print(data)
# longitude=data['iss_position']['longitude']
# latitude=data['iss_position']['latitude']

import requests
from datetime import datetime
import smtplib as st
import time
MY_LAT = 51.507351
MY_LONG = -0.127758
my_email= "sama29571@gmail.com"
my_password="gsmdsbqqawpdalyo"
while True:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    print(data)
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.


    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if iss_latitude == MY_LAT-10 and iss_longitude == MY_LONG-10 and time_now.hour >= sunset:
        with st.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email,#sending email to myself
                                msg=f"Subject:ISS IS HEREEE!!! \n\n Look up at the beautiful evening sky the ISS "
                                    f"tracker is passing over you.")
    time.sleep(60)




