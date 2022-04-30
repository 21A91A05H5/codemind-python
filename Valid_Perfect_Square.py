t=int(input())
for i in range(1,t+1):
    n=int(input())
    x=n**0.5
    if n%x==0:
        print("True")
    else:
        print("False")