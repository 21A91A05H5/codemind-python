n=int(input())
c=2
arr=list(map(int,input().split()))
for i in range(3,n):
    if arr[i]==arr[i-1]+arr[i-2]:
        c+=1
if c==n-1:
    print("yes")
else:
    print('no')