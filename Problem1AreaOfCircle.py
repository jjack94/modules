# James Jack
# 2/24/21

# Problem 1: Write a function areaOfCircle(r) which returns the area of a circle of radius r


def area_circle(r):
    import math
    a = math.pi * r ** 2  # formula for area of circle
    return a  # return statement used instead of print for definitive end


find_area = float(input("what is the radius? "))  # input is taken as float
ans = area_circle(find_area)
print(ans)
