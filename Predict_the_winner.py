n=int(input())
arr=list(map(int,input().split()))
sum1=0
sum2=0
for i in range(n//2):
    sum1+=arr[i]
for i in range(n//2,n):
    sum2+=arr[i]
x=abs(sum1-sum2)
if x%4==0:
    print("X")
else:
    print("Y")