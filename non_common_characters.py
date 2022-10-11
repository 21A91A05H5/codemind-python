s1=input().lower()
s2=input().lower()
a=''
for i in s1:
    if i not in s2 and i not in a and i!=' ':
        a+=i
for i in s2:
    if i not in s1 and i not in a and i!=' ':
        a+=i
print(''.join(sorted(a)))