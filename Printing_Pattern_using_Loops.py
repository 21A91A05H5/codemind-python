n=int(input())
for i in range(1,2*n):
    a=n
    for j in range(1,2*n):
        print(a,end=' ')
        if j<i:
            a-=1
        if j>(2*n-1-i):
            a+=1
    print()