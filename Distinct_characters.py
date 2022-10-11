a=input().lower()
s=''
for i in a:
    if a.count(i)==1 and i!=' ':
        s+=i
s=sorted(s)
print(''.join(s))