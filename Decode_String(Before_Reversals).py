n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    s=input()
    for i in range(b,0,-1):
        z=s[:i]
        z=z[::-1]
        z+=s[i:]
        s=z
    print(s)