def findhcf(a,b):
    if b==0:
        return a;
    return findhcf(b,a%b)
n=int(input())
arr=list(map(int,input().split()))
lcm=arr[0]
hcf=arr[0]
for i in range(1,n):
    hcf=findhcf(arr[i],lcm)
    lcm=(lcm*arr[i])//hcf
print(lcm)