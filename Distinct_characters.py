a=input().lower()
s=''
for i in a:
    if i not in s and i!=' ':
        s+=i
print(''.join(sorted(s)))