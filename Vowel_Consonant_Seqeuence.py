a=input().lower()
v="aeiou"
l=""
for i in a:
    if i in v:
        l+='V'
    else:
        l+="C"
q=''
for i in range(len(l)-1):
    if l[i]!=l[i+1]:
        q+=l[i]
print(q+l[-1])