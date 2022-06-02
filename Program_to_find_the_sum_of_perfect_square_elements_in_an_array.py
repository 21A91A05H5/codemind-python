import math
n=int(input())
sum=0
l=[]
arr=list(map(int,input().split()))
for i in arr:
    sq=int(math.sqrt(i))
    if sq*sq==i:
        sum=sum+i
print(sum)