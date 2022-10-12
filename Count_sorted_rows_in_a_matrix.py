l=[]
c=0
a,b=map(int,input().split())
for i in range(a):
    s=list(map(int,input().split()))
    l.append(s)
for i in l:
    if i==sorted(i) or i[::-1]==sorted(i):
        c+=1
print(c)