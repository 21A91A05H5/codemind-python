n=int(input())
c=0
arr=list(map(int,input().split()))[:n]
for i in range(n):
    c=0
    for j in range(n):
        if arr[j]<arr[i] and i!=j:
            c+=1
    print(c,end=' ')