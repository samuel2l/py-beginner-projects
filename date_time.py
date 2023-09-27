import datetime as dt
import random

#import time
#now() gets the current date and time
time_rn = dt.datetime.now()
print(time_rn)
#same as:
# print(time.ctime(time.time()))
# print(time.ctime())
#thiws module also has the  ctime function
print(time_rn.year)
print(time_rn.month)
print(time_rn.weekday())
#custom datetime obj to store my dob
dob= dt.datetime(year=2003,month=2,day=6,hour=18)
print(dob)

