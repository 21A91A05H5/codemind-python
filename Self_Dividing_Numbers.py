def self(n):
    c=0
    k=0
    x=n
    while n>0:
        d=n%10
        if d==0:
            return 0;
        elif x%d==0:
            c+=1
        k+=1
        n//=10
    if c==k:
        return 1;
    return 0; 
          
m=int(input())
n=int(input())
for i in range(m,n+1):
    if self(i):
        print(i,end=' ')
  
  
  
  
 