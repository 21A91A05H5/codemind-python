s1=input().lower()
s2=input().lower()
a=''
c=0
for i in s2.split():
    if i in s1.split():
        # print(i)
        c+=1
print(c)