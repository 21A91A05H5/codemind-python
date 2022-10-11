a=input().lower()
c=0
for i in a:
    if a.count(i)==1 and i!=' ':
        print(i)
        c=0
        break
    else:
        c=-1
if c==-1:
    print(c)