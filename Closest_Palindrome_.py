def palin(n):
    x=str(n)
    x=x[::-1]
    x=int(x)
    if n==x:
        return 1
    else:
        return 0
n=int(input())
for i in range(n+1,2*n+1):
    if palin(i):
        front=i
        break
for i in range(n-1,9,-1):
    if palin(i):
        back=i
        break
if (n-back)<(front-n):
    print(back)
elif (n-back)>(front-n):
    print(front)
else:
    print(back,front)