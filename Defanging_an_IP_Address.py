n=input()
n=list(n)
l=[]
for i in n:
    if i=='.':
        l.append('[.]')
    else:
        l.append(i)
print(''.join(l))