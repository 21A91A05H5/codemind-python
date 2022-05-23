str=input()
c=input()
d=0
s=0
for i in range(len(str)):
    if str[i]==c:
        d+=1
    else:
        s=0
if d>0:
    print(d)
else:
    print('-1')