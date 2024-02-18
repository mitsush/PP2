# Write a Python program to calculate the area of a trapezoid.


import math

def area_of_the_trapezoid(height = 5, first_base = 5, second_base = 6) -> float:
    area = ((first_base + second_base)/2)*height

    return area

print(area_of_the_trapezoid())
