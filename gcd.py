import math

l = []
b = 90
for i in range(1,91):
    h = math.gcd(i, b)
    if h == 1:
        l.append(i)
        
print(l)