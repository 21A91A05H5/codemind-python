import array as arr
n=int(input())
sum=0
arr=[]
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum>n:
    print("True")
else:
    print("False")