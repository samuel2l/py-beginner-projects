import smtplib
my_email= "sama29571@gmail.com"
my_password="ynglmgyiscxlrnmp"
with smtplib.SMTP("smtp.gmail.com") as connection:

    #argtxt_toument passed in SMTP is the location of your email providers SMTP server
    #to secure our connection to the email server we use TLS(transfer layer security)
    connection.starttls()
    connection.login(user=my_email ,password=my_password)
    connection.sendmail(from_addr=my_email,to_addrs=" ",msg="Subject:First Python Mail \n\n Sending you a  mail using python")

