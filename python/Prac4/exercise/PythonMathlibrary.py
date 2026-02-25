#1.Write a Python program to convert degree to radian.

import math

degree = 15
radian = degree * (math.pi / 180)

print("Input degree:", degree)
print("Output radian:", radian)

#2.Write a Python program to calculate the area of a trapezoid.
height = 5
base1 = 5
base2 = 6

area = 0.5 * (base1 + base2) * height

print("Area of trapezoid:", area)

#3.Write a Python program to calculate the area of regular polygon.

import math

n = 4            
s = 25         

area = (n * s * s) / (4 * math.tan(math.pi / n))

print("The area of the polygon is:", area)

#4.Write a Python program to calculate the area of a parallelogram.

base = 5
height = 6

area = base * height

print("Area of the parallelogram:", float(area))
