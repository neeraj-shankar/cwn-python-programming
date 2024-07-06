
import datetime
time = datetime.datetime.utcnow()
print(time.minute)
print(time)
#time = time.replace(second=0,microsecond=0,minute=int(time.minute/15)*15)
print(time)

timestamp = int(time.timestamp())
print(timestamp)