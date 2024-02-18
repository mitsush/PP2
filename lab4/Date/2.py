# Write a Python program to print yesterday, today, tomorrow.


from datetime import *

class Time():
    def yesterday():
        print(datetime.today() - timedelta(days = 1))

    def today():
        print(datetime.today())

    def tomorrow():
        print(datetime.today() + timedelta(days = 1))


Time.yesterday()
Time.today()
Time.tomorrow()
