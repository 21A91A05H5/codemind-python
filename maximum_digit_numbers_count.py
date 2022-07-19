n=int(input())
a=list(map(str,input().split()))
l=[]
z=[]
for i in a:
    l.append(len(i))
for i in range(n):
    if l[i]==max(l):
        z.append(a[i])
print(*z)