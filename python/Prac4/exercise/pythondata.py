#1.Write a Python program to subtract five days from current date.



import datetime

current_date = datetime.datetime.now()

new_date = current_date - datetime.timedelta(days=5)

print("Current date:", current_date)
print("Five days ago:", new_date)

#2.Write a Python program to print yesterday, today, tomorrow.

import datetime

today = datetime.date.today()

yesterday = today - datetime.timedelta(days=1)

tomorrow = today + datetime.timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#3.Write a Python program to drop microseconds from datetime.

import datetime

now = datetime.datetime.now()

clean_time = now.replace(microsecond=0)

print("Original datetime:", now)
print("Without microseconds:", clean_time)

#4.Write a Python program to calculate two date difference in seconds

import datetime

date1 = datetime.datetime(2026, 2, 25, 12, 0, 0)

date2 = datetime.datetime(2026, 2, 25, 15, 30, 0)

difference = (date2 - date1).total_seconds()

print("Difference in seconds:", difference)
