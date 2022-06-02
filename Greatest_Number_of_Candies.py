n=int(input())
arr=list(map(int,input().split()))[:n]
m=int(input())
for i in range(0,len(arr)):
    if arr[i]+m>=max(arr):
        print("True",end=' ')
    else:
        print("False",end=' ')