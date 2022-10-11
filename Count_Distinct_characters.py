a=input().lower()
s=''
for i in a:
    if i not in s and i!=' ':
        s+=i
print(len(s))