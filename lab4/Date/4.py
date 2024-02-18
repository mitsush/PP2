# Write a Python program to calculate two date difference in seconds.


import datetime
import time

def difference_between_two_dates():
    current_datetime = datetime.datetime.today().replace(microsecond=0)

    time.sleep(5)

    other_datetime = datetime.datetime.today().replace(microsecond=0)

    return (other_datetime - current_datetime).total_seconds()

print(difference_between_two_dates())
