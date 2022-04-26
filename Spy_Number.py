n=int(input())
sum1=1
sum2=0
while n>0:
    d=n%10
    sum1=sum1*d
    sum2=sum2+d
    n=n//10
    
if(sum1==sum2):
    print("Spy Number")
else:
    print("Not Spy Number")