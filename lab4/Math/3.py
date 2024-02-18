# Write a Python program to calculate the area of regular polygon.


from math import tan, tanh

def area_of_the_polygon(num_sides = 4, len_sides = 25) -> float:

    apothem = len_sides/(2*tanh(180/num_sides))  
    perimeter = num_sides * len_sides
    area = (perimeter * apothem)/2
        
    return area


print(area_of_the_polygon(4, 25))

