#Hbase: 0.9x or greater

# Creating Data

# Format is replication
# Timestamp, x,y,z at a rate of 25Hz


import csv
import datetime
import time
import random

with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    #DateTime =datetime.datetime(2017,1,1,0,0,0,0) #year, month, day, hr, minute, second, microsecond
    TimeStamp=1483228800000
    for i in range(0,1000):
        accx=random.uniform(0,10.0)
        accy=random.uniform(0,10.0)
        accz=random.uniform(0,10.0)
        #timestamp=round(DateTime.time()*1000)
        writer.writerow([TimeStamp, accx, accy, accz])
        TimeStamp=TimeStamp+40
        #DateTime=DateTime+datetime.timedelta(milliseconds=40)
        #print(DateTime)
