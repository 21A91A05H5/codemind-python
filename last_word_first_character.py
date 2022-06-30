n=input()
c=0
l=[]
for i in n.split():
    l.append(i)
x=len(l)
a=l[x-1]
for i in a:
    print(i)
    break