m,n=map(int,input().split())
c=0
p=list(map(int,input().split()))
q=list(map(int,input().split()))
a=[]
b=[]
for i in p:
    if i not in a:
        a.append(i)
for i in q:
    if i not in b:
        b.append(i)
for i in b:
    if i in a:
        c+=1
print(c)