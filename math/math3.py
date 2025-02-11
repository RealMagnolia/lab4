import math

n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
area = int(n) * int(l)**2 / (4 * math.tan(math.pi / int(n)))

print(f"The area of the polygon is: {round(area)}")