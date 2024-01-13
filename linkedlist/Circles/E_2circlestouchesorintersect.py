'''
 if two given circles touch or intersect each other
'''
import math
 
# Function to check if two circles touch each other
def circle(x1, y1, x2, y2, r1, r2):
    d = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
 
    if(d <= r1 - r2):
        print("Circle B is inside A")
    elif(d <= r2 - r1):
        print("Circle A is inside B")
    elif(d < r1 + r2):
        print("Circle intersect to each other")
    elif(d == r1 + r2):
        print("Circle touch to each other")
    else:
        print("Circle not touch to each other")
 