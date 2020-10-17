import math
import time

start_time = time.time()

def factor(number):
    count = 2
    if number == 1:
        count = 1
    elif number == 3:
        count = 2
    elif number == 6:
        count = 4
    elif number % 2 == 0:
        count += 2
    elif number % 3 == 0:
        count += 2
    for j in range(4, int(math.sqrt(number)+1)):
        if number % j == 0:
            count += 2
    return count


found = False
i = 1
p = 1
while not found:
    if factor(i) > 500:
        found = True
    else:
        p += 1
        i += p

total_time = time.time() - start_time
print(f"We found it baby {i} in {round(total_time,3)} seconds")

