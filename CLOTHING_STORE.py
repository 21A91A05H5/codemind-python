#include<stdio.h>
n=int(input())
c=0
arr=list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        if arr[i]==arr[j] and i!=j and arr[i]>0:
            c+=1
            arr[j]=0
            break
print(c)