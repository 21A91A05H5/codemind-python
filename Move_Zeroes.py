l=[]
l1=[]
n=int(input())
arr=list(map(int,input().split()))
for i in range(len(arr)):#1 2 3 0 0 5 6 7
    if arr[i]!=0: 
        l.append(arr[i])
    else:
        l1.append(arr[i])
x=l+l1
print(*x)