import pytz

all_timezones = pytz.all_timezones
print(all_timezones)

# with open("timezones.txt", "w") as file:
#     for tz in all_timezones:
#         file.write(f"{tz}\n")