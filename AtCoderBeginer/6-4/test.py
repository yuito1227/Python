import datetime

target_day = str(input())
# target_day = "20220527"
tg_date = datetime.datetime.strptime(target_day, "%Y%m%d")
td_date = datetime.datetime.now()


tg_weekday = tg_date.strftime("%A")
td_weekday = td_date.strftime("%A")
print(f"Target {tg_weekday}")
print(f"Target {td_weekday}")
d_date = (td_date - tg_date).days
print(f"Delta days is {d_date} days")
