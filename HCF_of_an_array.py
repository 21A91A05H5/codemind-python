n=int(input())
arr=list(map(int,input().split()))[:n]
m=min(arr)
while True:
    c=0
    for i in range(n):
        if arr[i]%m==0:
            c+=1
    if c==n:
        break
    else:
        m-=1
print(m)