import math
n=int(input())
c=0
temp=n
while n>0:
    d=n%10
    c=c+1
    n=n//10
n=temp
sum=0

while n>0:
    r=n%10
    sum=sum+math.pow(r,c)
    n=n//10
    c=c-1
if sum==temp:
    print('True')
else:
    print('False')