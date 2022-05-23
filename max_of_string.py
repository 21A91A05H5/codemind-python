str=input()
c=0
for i in range(len(str)):
    if ord(str[i])>c:
        c=ord(str[i])
print(chr(c))