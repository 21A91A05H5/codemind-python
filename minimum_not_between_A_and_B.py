n=int(input())
s=[]
l=list(map(int,input().split()))
a,b=map(int,input().split())
for i in l:
    if i<a or i>b:
        s.append(i)
if len(s)!=0:
    print(min(s))
else:
    print(-1)