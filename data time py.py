from datetime import date
#date object of today's date
today= date.today()
print(today)
print("current year:",today.year)
print("current month:",today.month)
print("current day:",today.day)

import datetime
datetime_object=datetime.datetime.now()
print(datetime_object)
x=datetime.datetime.now()
print(x.strftime("%B"))
