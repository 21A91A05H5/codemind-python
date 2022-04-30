m=int(input())
n=int(input())
sum=0
for i in range(m,n+1,1):
    temp=i
    sum=0
    while temp>0:
        d=temp%10
        sum=sum*10+d
        temp//=10
    if i==sum:
        print(i,end=' ')