n=input()
#print(n)
a=set("@_#$!%^&*.|")
c=0
for i in range(len(n)):
    if n[i] in a:
        c+=1
print(c)