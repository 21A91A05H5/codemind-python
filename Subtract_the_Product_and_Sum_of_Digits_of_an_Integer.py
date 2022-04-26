n=int(input())
sum1=1
sum2=0
while n>0:
    d=n%10
    sum1=sum1*d
    sum2=sum2+d
    n=n//10
    
c=sum1-sum2
print(c)