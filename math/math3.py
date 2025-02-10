import math

n, l = input().split()
area = (int(n)*int(l)**2)/(4*math.tan(math.pi/int(n)))

print(round(area))