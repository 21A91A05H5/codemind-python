import math
a,b,c=map(int, input().split())
l=math.pow(a,b)
d=int(l%c)
print(d)