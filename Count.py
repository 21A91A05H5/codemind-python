n=int(input())
c=0
d=0
arr=list(map(int,input().split()))[:n]
for i in range(n):
    if arr[i]%2==0:
        c+=1
    elif arr[i]%2!=0:
        d+=1
print(c,d)
    