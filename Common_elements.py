a,b=map(int,input().split())
l=(list(map(int,input().split())))
m=(list(map(int,input().split())))
c=0
s=[]
for i in (l):
    if i in m and i not in s:
        # print(i,end=' ')
        s.append(i)
print(*s)
# for i in set(m):
#     if i in l:
#         print(i,end=' ')