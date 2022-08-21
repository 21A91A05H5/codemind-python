n=int(input())
x=[]
l=list(map(int,input().split()))
for i in l:
    if i not in x:
        x.append(i)
for i in x:
    print(i,l.count(i),end=' ')
    