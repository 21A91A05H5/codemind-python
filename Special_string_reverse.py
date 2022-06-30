n=input()
a=list(n)
alp=[]
sp=[]
index=[]
for i in range(len(a)):
    if a[i].isalpha():
        alp.append(a[i])
    else:
        sp.append(a[i])
        index.append(i)
alp=alp[::-1]
for i in range(len(index)):
    alp.insert(index[i],sp[i])
print(*alp,sep='')