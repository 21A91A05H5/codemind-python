n=int(input())
for i in range(n):
    m=int(input())
    c=0
    arr=list(map(int,input().split()))
    for j in range(1,m):
        if arr[j]<arr[j-1]:
            c+=1
    if c==0:
        print(c)
    else:
        print(max(arr)-min(arr))