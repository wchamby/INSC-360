# (1)
# William Chase Hamby
# 2/10/20
# homework-3.py
# -*- coding: utf-8 -*-
# This is the description for homework 3

from datetime import date
from datetime import datetime
import calendar
import time

# (2)
today_date = date.today()
print(today_date)

# (3)
today_date_string = today_date.strftime("%m/%d/%Y")
print(today_date_string)

# (4)
graduation = "May 15, 2020"
print(graduation)

# (5)
graduation = "5-15-2020"
datetime.strptime(graduation, '%m-%d-%Y')
print(graduation)

#(6)
graduation_month = 5
graduation_day = 15
graduation_year = 2020
print("Month: " + str(graduation_month))
print("Day: " + str(graduation_day))
print("Year: " + str(graduation_year))

#(7)
import datetime
weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
today_weekday = datetime.date(2020,2,10)
today_weekday_plus = today_weekday.weekday()
today_weekday_AsString = weekDays[today_weekday_plus]
print("Today's class is on a {}".format(today_weekday_AsString))
