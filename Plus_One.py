n=int(input())
s=[]
p=0
a=list(map(int,input().split()))
for i in range(len(a)):
    p=p*10+a[i]
k=p+1
while(k):
    r=k%10
    s.append(r)
    k=k//10
for i in range(len(s)-1,-1,-1):
    print(s[i],end=" ")