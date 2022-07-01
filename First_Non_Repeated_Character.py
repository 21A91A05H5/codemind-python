t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    for j in s:
        c=0
        for k in s:
            if j==k and (j.isdigit()==False) and (k.isdigit()==False):
                c+=1
        if c==1:
            print(j)
            break
    else:
        print("-1")