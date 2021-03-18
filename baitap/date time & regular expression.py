# date & time
import datetime

#lấy ngày giờ hiện tại
dt_now = datetime.datetime.now()
print(dt_now)

#lấy ngày hiện tại
dt_today = datetime.date.today()
print(dt_today)

# set ngày tháng
day = datetime.date(2021,1,23)
print(day)

# lấy ngày ,tháng ,năm
today = datetime.date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

#lớp time

from datetime import time

x = time()
print("x=",x)

y = time(23,30,30)
print("y=",y)

z = time(23,30,30,3647)
print("z=",z)

#lớp datetime
from datetime import datetime

#datetime(year, month, day)
a = datetime(2018, 11, 28)
print(a)

# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime(2021, 1, 28, 23, 55, 59, 342380)
print(b)

#timedelta

from datetime import datetime, date

t1 = date(year = 2021, month = 2, day = 12)
t2 = date(year = 2017, month = 12, day = 23)
t3 = t1 - t2
print("t3 =", t3)

t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2021, month = 2, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print("t6 =", t6)


from datetime import timedelta

t1 = timedelta(weeks = 3, days = 3, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2

print("t3 =", t3)

#định dạng ngày giờ stftime
timenow = datetime.now()

t1 = timenow.strftime("%H:%M:%S")#hour/minute/second
t2 = timenow.strftime("%S:%M:%H")#second/minute/hour
print("time:", t1)
print("time:", t2)

s1 = timenow.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format day/month/year
print("s1:", s1)

s2 = timenow.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format month/day/year
print("s2:", s2)

#regular expression

# ham findall()

import re

text1 = "this is my friend"
result1 = re.findall("friend", text1)
print(result1)

# ham search()

text2 = "the beauty flowers in the hill"
result2 = re.search("beauty", text2)
print(result2)

print(result2.span())

print(result2.group())

print(result2.string)

#ham split()

text3 = "hello everyone, my name is jack"
result3 = re.split("\s",text3)
print(result3)

#ham sub()

text4 = "vietnam belongs to southeast asia"
result4 = re.sub("\s","-",text4)
print(result4)