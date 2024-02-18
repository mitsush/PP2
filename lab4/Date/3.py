# Write a Python program to drop microseconds from datetime.


import datetime

def no_microseconds(current_datetime):
    return current_datetime.replace(microsecond = 0)

print(no_microseconds(datetime.datetime.today()))
