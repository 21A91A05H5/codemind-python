a,b=map(int,input().split())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
c=0
for i in (l):
    if i not in m:
        print(i,end=' ')
for i in (m):
    if i not in l:
        print(i,end=' ')
