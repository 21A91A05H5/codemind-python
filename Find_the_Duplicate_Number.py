n=int(input())
arr=list(map(int,input().split()))
c=0
l1=[]
for i in arr:
    if i not in l1:
        l1.append(i)
    else:
        print(i,end=' ')