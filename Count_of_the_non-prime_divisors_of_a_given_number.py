n=int(input())
e=0
c=0
d=0
for i in range(1,n+1):
    if(n%i==0):
        c+=1
        d=0
        for j in range(1,i+1):
            if(i%j==0):
                d+=1
        if(d==2):
            e+=1
print(c-e)