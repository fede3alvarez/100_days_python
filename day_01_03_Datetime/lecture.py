from datetime import datetime
from datetime import date

print("datetime.today() gives you today's date:")
today = datetime.today()
print(today)

print("the type is:")
print(type(today))
print("")

print("date.today() gives you today's date:")
today_date = date.today()
print(today_date)

print("the type is:")
print(type(today_date))

christmas = date(2022,12,25)
ollie_bday = date(2022,1,6)

print("")
print("Day until christmas: ", christmas - today_date)
print("Today Ollie is: ", today_date - ollie_bday)