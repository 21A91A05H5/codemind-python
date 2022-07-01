n=input()
n=n.lower()
c=0
d=0
l=['a','e','i','o','u']
for i in range(len(n)):
    c=0
    if n[i] in l:
        for j in range(i,len(n)):
            if n[j] in l:
               c+=1
            else:
                break
        if c>d:
            d=c
print(d)