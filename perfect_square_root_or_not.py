import math
number = int(input())
root = math.sqrt(number)
if int(root + 0.9999) ** 2 == number:
    print("True")
else:
    print("False")