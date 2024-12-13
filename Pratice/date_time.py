import datetime
currentdatetime=datetime.datetime.now()
print(currentdatetime.strftime("%d/%m/%Y"))

date1=datetime.datetime(2025,10,1)
date2=datetime.datetime(2024,10,1)
difference=date1-date2+datetime.timedelta(hours=10)
print (difference)