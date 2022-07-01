n=input()
d=0
c=0
for i in n:
    if i=='z':
        c+=1
    if i=='o':
        d+=1
if d==2*c:
    print("Yes")
else:
    print("No")