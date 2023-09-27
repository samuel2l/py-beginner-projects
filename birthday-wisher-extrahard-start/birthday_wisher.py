#COME BACK AND RUN IT ON THE CLOUD
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import pandas as pd
import random
import datetime as dt
import smtplib as st
my_email= "sama29571@gmail.com"
my_password="ynglmgyiscxlrnmp"

data= pd.read_csv('birthdays.csv')
#names_list=data["name"].to_list()

# possible_birthday_day=data[data.day == bday_day].day
# possible_birthday_month=data[data.day == bday_month].month
now = dt.datetime.now()
curr_month = now.month
curr_day = now.day

letter_list = ["letter_1", "letter_2", "letter_3"]

for index,row in data.iterrows():

    if row.day==curr_day and row.month== curr_month:
        print(row.myname)
        rand_letter = random.choice(letter_list)
        with open(f"letter_templates/{rand_letter}.txt") as file:
            content=file.read()
            new_letter=content.replace("[NAME]",f"{row.myname}")
        #you could also use readlines to make it a list and target the first index to change but this is simpler
            print(new_letter)
        with st.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email,  # sending email to myself
                                msg=f"HAPPY BIRTHDAYY \n\n {new_letter}")

