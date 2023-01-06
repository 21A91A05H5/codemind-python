a=input()
n=int(input())
x=n//len(a)
t=a.count('a')*x
t+=a[:n%len(a)].count('a')
print(t)