import datetime as dt
input()
time1 = dt.datetime.now()
input()
time2 = dt.datetime.now()
dif = time2 - time1
print(abs(dif.seconds))
#datetime.timedelta()

a = dt.datetime(2013,12,30,23,59,59)
b = dt.datetime(2013,12,31,23,59,59)

print((b-a).total_seconds())