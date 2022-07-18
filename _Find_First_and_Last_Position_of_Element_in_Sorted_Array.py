n=int(input())
l=list(map(int,input().split()))
a=int(input())
c=0
for i in range(0,n):
    if l[i]==a:
        print(i,end=' ')
        break
else:
    print(-1,end=' ')
for i in range(n-1,-1,-1):
    if l[i]==a:
        print(i,end=' ')
        break
else:
    print(-1)