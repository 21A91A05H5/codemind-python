n=int(input())
s=[]
l=list(map(int,input().split()))
# m=list(map(int,input().split()))
for i in range(0,len(l),2):
    for j in range(l[i+1]):
        s.append(l[i])
print(*s)