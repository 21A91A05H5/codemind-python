a,b=map(int,input().split())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
s=[]
for i in (l):
    if i in m and i not in s:
        s.append(i)
# for i in set(m):
#     if i not in l:
#         c+=1
print(*s)