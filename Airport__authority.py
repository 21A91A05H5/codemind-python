t=int(input())
l=[]
c=0
for i in range(t):
    l.append(int(input()))
w=int(input())
for i in range(t):
    if l[i]<=w:
        c+=1
    elif l[i]>w:
        c=c+2
print(c)