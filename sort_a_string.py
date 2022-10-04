s=[]
x=[]
q=[]
a=list(input())
for i in range(len(a)):
    if a[i].isalpha():
        s.append(a[i])
    else:
        x.append(i)
        q.append(a[i])
s=sorted(s)
for i in range(len(x)):
    s.insert(x[i],q[i])
print("".join(s))