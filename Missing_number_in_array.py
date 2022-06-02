t=int(input())
for i in range(t):
    n=int(input())
    l=[]
    arr=list(map(int,input().split()))
    for i in range(1,n+1):
        l.append(i)
    for i in l:
        if i not in arr:
            print(i)