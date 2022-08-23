s=input()
c=0
l=''
for i in s.split():
    if c%2==0:
        l+=i[::-1]
    else:
        l+=i
    l+=' '
    c+=1
print(l.rstrip())