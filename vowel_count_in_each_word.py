n=input()
n.lower()
l=[]
c=0
s=set("aeiou")
for i in n.split():
    c=0
    for j in i:
        if j in s:
            c+=1
    l.append(c)
print(*l)