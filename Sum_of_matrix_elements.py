n=int(input())
m=int(input())
sum=0
arr=[list(map(int,input().split()))
for i in range(n)]
for i in range(n):
    for j in range(m):
        sum=sum+arr[i][j]
print(sum)