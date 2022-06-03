def product(n,arr):
    pr=1
    for i in range(len(arr)):
        if arr[i]!=n:
            pr=pr*arr[i]
    return pr
    
n=int(input())
arr=list(map(int,input().split()))
for i in arr:
    print(product(i,arr),end=' ')