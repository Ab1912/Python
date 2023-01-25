# Date time in python

#1. Date functions
#2. Time functions
#3. Date & Time functions
#4. Differeance in date & time
#5. Date & time format

import datetime as dt

#1. Date functions
print("1. Date functions : ")
# current date
date1 = dt.date.today()
print("Current Date : ",date1)
print("---------------------")

date2 = dt.date(1995,6,21)
print("Date : ",date2)
print("Day : ",date2.day)
print("Month : ",date2.month)
print("Year : ",date2.year)
print("---------------------")

#2. Time functions
print("Time functions : ")
time1 = dt.time(10,17,45,5548)
print("Time : ",time1)
print("Hour : ",time1.hour)
print("Minutes : ",time1.minute)
print("Seconds : ",time1.second)
print("Microseconds : ",time1.microsecond)
print("---------------------")

#3. Date & Time functions
print("3. Date & Time functions")
print("Current date & time : ")
date_time1 = dt.datetime.now()
print(date_time1)
print("---------------------")

date_time2 = dt.datetime(1986,10,12,4,3,32,48943)
print("Date & Time : ",date_time2)
print("Day : ",date_time2.day)
print("Month : ",date_time2.month)
print("Year : ",date_time2.year)
print("Hour : ",date_time2.hour)
print("Minutes : ",date_time2.minute)
print("Seconds : ",date_time2.second)
print("Microseconds : ",date_time2.microsecond)
print("---------------------")

#4. Differeance in date & time
print("4. Differeance in date & time : ")
new_yr = dt.datetime(2024,1,1)
current_yr = dt.datetime.now()
countdown = new_yr - current_yr
print("New Year Countdown : ",countdown)
print("---------------------")

#5. Date & time format
print("5. Date & time format : ")
date_time3 = dt.datetime(1986,10,12,16,2,12,4787)
dt_format = date_time3.strftime("%d %b %Y %I %M %S %f %p")
print("Date & Time format : ",dt_format)