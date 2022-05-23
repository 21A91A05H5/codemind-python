str=input()
c=0
vowels=set("aeiouAEIOU")
for i in str:
    if i in vowels:
        c+=1
print(c)