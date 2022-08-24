s=input().split()
a=s[0]
b=s[len(s)-1]
l=[]
for i in a:
    l.append(ord(i))
print(chr(min(l)),end=' ')
l=[]
for i in b:
    l.append(ord(i))
print(chr(max(l)))