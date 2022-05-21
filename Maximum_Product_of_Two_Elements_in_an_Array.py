arr=list(map(int,input().split()))
max=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if (arr[i]-1)*(arr[j]-1)>max:
            max=(arr[i]-1)*(arr[j]-1)
print(max)