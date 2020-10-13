top = 1000
total = 0

for i in range(top):
    print(i)
    if (i % 3) == 0:
        total = total + i
    elif (i % 5) == 0:
        total = total + i

print(total)