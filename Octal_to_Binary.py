n=int(input())
for _ in range(n):
    a=input()
    a=int(a,8)
    print(bin(a)[2:])