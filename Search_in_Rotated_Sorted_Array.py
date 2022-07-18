n=int(input())
l=list(map(int,input().split()))
x=int(input())
c=0
for i in range(n):
    if l[i]==x:
        c=i
        break
if c>0:
    print(c)
else:
    print(-1)