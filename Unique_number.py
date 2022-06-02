n=int(input())
n=list(str(n))
m=list(set(n))
if len(n)==len(m):
    print("Unique Number")
else:
    print("Not Unique Number")