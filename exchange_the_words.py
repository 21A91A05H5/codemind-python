n=input()
l=n.split()
# // for i in range(len(l)):
# //     l[i]=(l[i][::-1])
for i in range(len(l)-1,-1,-1):
    print(l[i],end=' ')