n=int(input())
sum=0
sq=n*n
while(sq>0):
    sum=sum+(sq%10)
    sq=sq//10
if(sum==n):
    print("Neon Number")
else:
    print("Not Neon Number")