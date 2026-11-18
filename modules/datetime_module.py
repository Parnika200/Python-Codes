import datetime

print(datetime.date.today())
print(datetime.datetime.now()) #date + time
print(datetime.time())

date=datetime.date.today()
print(date.day)
print(date.month)
print(date.isoweekday())


#TIMEDELTA - perform arithmetic operations on date

# add 10 days
today=datetime.date.today()
new=today+datetime.timedelta(days=10)
print(new)

# sub 10 days
t=datetime.date.today()
n=t-datetime.timedelta(days=5)
print(n)

#diff between 2 dates

d1=datetime.date(2026,10,1)
d2=datetime.date(2025,10,1)
diff=d1-d2
print(diff.days)