# Write a Python program to subtract five days from current date.


from datetime import datetime, timedelta

def minus_five_of_current_datetime(current_datetime):
    return current_datetime - timedelta(days = 5)

print(minus_five_of_current_datetime(datetime.today()))
