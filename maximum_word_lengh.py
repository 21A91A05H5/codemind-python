n=input()
c=0
l=[]
s=[]
# max=0
for i in n.split():
    l.append(i)
    x=len(i)
    s.append(x)
print(max(s))