#Example
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

#1
import datetime

x = datetime.datetime.now()

print(x.month)
print(x.day)

#2
import datetime

x = datetime.datetime.now()

print(x.weekday())

#3
import datetime

x = datetime.datetime.now()

print(x.strftime("%B"))

#4
import datetime

x= datetime.datetime.now()

print(x.strftime("%H:%M:%S"))

#5

import datetime

x = datetime.datetime.now()

print(x.strftime("%d-%m-%Y, %A"))

#Example
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

#1
import datetime

x = datetime.datetime(2023, 1, 1)
print(x)

#2
import datetime

x = datetime.datetime(2021, 12, 31, 23, 59, 59)
print(x)

#3
import datetime

x = datetime.datetime(2022, 8, 10)
print(x.strftime("%A"))

#4

import datetime

x = datetime.datetime(2019, 3, 15)
print(x.strftime("%B"))

#5

import datetime

x = datetime.datetime(2018, 7, 20)

print(x.year)
print(x.month)
print(x.day)

#Example
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

#1
import datetime

x = datetime.datetime(2007, 12, 5)

print(x.strftime("%d"))

#2
import datetime

x = datetime.datetime(2019, 11, 4)
print(x.strftime("%A"))

#3
import datetime

x = datetime.datetime(2020, 2, 14)
print(x.strftime("%d %B %Y"))

#4
import datetime

x = datetime.datetime(2017, 9, 10)
print(x.strftime("%m"))

#5
import datetime

x = datetime.datetime(2007, 11, 2)
print(x.strftime("%Y"))

