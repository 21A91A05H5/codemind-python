a,b=map(int,input().split())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
c=0
for i in set(l):
    if i not in m:
        c+=1
for i in set(m):
    if i not in l:
        c+=1
print(c)