s=input()
s=s.lower()
a="aeiou"
a=list(a)
k=0
for i in s:
    if i in a:
        a.remove(i)
if len(a)==0:
    print(0)
else:
    for i in range(len(a)):
        print(a[i],end=' ')