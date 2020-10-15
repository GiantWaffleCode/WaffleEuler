import math
a = 1
b = 2
c = 3

for b in range(2, 1001, 1):
    for a in range(1, b, 1):
        if 1000 - a - b == math.sqrt(a**2 + b**2):
            c = 1000 - a - b
            answer = a * b * c
            print(f"Answer is {answer}")


