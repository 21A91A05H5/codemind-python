n=int(input())
i=0;sum=0
while n!=0:
    d=n%10
    sum=sum+d*(8**i)
    n=n//10
    i=i+1
print('{:b}'.format(sum))