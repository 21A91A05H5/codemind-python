def pretty(n):
    temp=n
    c=0
    while temp!=0:
        d=temp%10
        if d==2 or d==3 or d==9:
            c+=1
        break
    if c==1:
        return 1
t=int(input())
c=0
for i in range(t):
    c=0
    a,b=map(int,input().split())
    for j in range(a,b+1):
        if pretty(j):
            c+=1
    print(c)