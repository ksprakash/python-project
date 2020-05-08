from datetime import datetime
import pytz

time_utcnow=datetime.now(tz=pytz.UTC)
print(time_utcnow)

time_estnow=time_utcnow.astimezone(tz=pytz.timezone(zone='US/Eastern'))
print(time_estnow)


time_est=datetime.now(tz=pytz.timezone(zone='US/Eastern'))
print(time_est)

#append actually changes the list. Also, it takes an item, not a list. Hence, all you need is
regions=[]
print("==================================================================================================")
for zone in pytz.all_timezones:
    regions.append(zone)

print(regions)

#I personally prefer the + operator than append:

regions=[]
print("==================================================================================================")

for zone in pytz.all_timezones:
    regions = regions + [zone]

print(regions)