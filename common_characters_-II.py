a=input().lower()
b=input().lower()
c=0
d=''
for i in b:
    if i in a and i not in d and i!=' ':
        c+=1
        d+=i
print(c)