import datetime

friday = 4
year = 1634
count = 0
for i in range(1, 13):
    if datetime.date(year,i,13).weekday()==friday:
        count +=1
print(count)
