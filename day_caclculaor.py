from datetime import datetime

# first_day = date (1984,1,16)
# last_day = date (2022,12,22)

# sum = first_day - last_day

# x = sum


# print(sum)

today_date = datetime.date(1984,1,16)
date_obj =datetime.date(2022,12,22)

delta = date_obj - date_obj
print(delta.days)
