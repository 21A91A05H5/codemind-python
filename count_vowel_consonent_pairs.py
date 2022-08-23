s=input()
v='aeiou'
s.lower()
n=len(s)
c=0
for i in range(n//2):
    if (s[i] in v and s[n-1-i]!=' ' and s[n-i-1] not in v) or (s[i] not in v and s[i]!=' ' and s[n-i-1] in v):
        c+=1
print(c)