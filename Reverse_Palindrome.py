def reverse(x:int)->int:
    temp=x                                       #finding reverse of a number
    rev=v=0
    if x<0:
        x=-x
        v=1
    while(x!=0):
        d=x%10
        rev=(rev*10)+d
        x=x//10
    x=temp
    if v==1:
        rev=-rev
        return rev
    else:
        rev=rev
        return rev
def palin(n):
    sum=0
    temp=n
    while n>0:
        d=n%10
        sum=sum*10+d
        n//=10
    if sum==temp:
        return True
    else:
        return False
n=int(input())
while True:
    a=reverse(n)
    x=a+n
    if palin(x):
        print(x)
        break
    else:
        n=x
