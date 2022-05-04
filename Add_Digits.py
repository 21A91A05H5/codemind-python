def digsum(n):
    sum=0
    while(n>0 or sum>9):
        if(n==0):
           n,sum=sum,n
        d=n%10
        sum+=d
        n//=10
    return sum
n=int(input())
print(digsum(n))