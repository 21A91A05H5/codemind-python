a=0
s1=input().lower()
s2=input().lower()
l=''
# s1=set(list(s1))
# s2=set(list(s2))
# a=list(s1.intersection(s2))
# a.remove(' ')
# print(''.join(sorted(a)))
for i in s1:
    if i!=' ' and i not in s2 and i not in l:
        l+=i
        a+=1
for i in s2:
    if i not in s1 and i!=' 'and i not in l:
        l+=i
        a+=1
print(a)
# print(s2)
