import math

a = int(input())
b = int(input())

c = str(int(round(math.degrees(math.atan2(a,b))))) + '°'
print(c)
