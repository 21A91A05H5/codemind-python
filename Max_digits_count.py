n=int(input())
arr=list(map(int,input().split()))[:n]
l=[]
for i in range(n):
    c=0
    while(arr[i]>0):
        d=arr[i]%10
        arr[i]//=10
        c+=1
    l.append(c)
print(l.count(max(l)))