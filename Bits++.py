t=int(input())
b=0
for i in range(t):
    a=input()
    for i in a:
        if i=='+':
            b+=1
        elif i=='-':
            b-=1
print(b//2)