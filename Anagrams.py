def anagram(s,s1):
    for char in s:
        if char not in s1:
            return False
    return True
s=input()
s1=input()
s=s.lower()
s1=s1.lower()
if anagram(s,s1):
    print('True')
else:
    print('False')