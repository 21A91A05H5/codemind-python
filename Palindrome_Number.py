t=int(input())
for i in range(1,t+1):
    n=int(input())
    sum=0
    temp=n
    while n>0:
        d=n%10
        sum=sum*10+d
        n//=10
    if sum==temp:
        print("True")
    else:
        print('False')