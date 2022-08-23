s=input().split()
c=0
for i in s:
    n=len(i)
    i.lower()
    for j in range(n//2):
        if (i[j] in 'aeiou' and i[n-j-1]!=' ' and i[n-j-1] not in 'aeiou') or (i[j] not in 'aeiou' and i[j]!=' ' and i[n-j-1] in 'aeiou'):
            c+=1
print(c)