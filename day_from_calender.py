#this will calculate the todays day of the week 
from datetime import date
import calendar
my_date = date.today()
my_date = date(2016,12,31)
print(calendar.day_name[my_date.weekday()])