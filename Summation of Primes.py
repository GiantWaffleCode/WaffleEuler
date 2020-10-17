import math


def is_prime(number):
    if number == 1:
        return False
    for j in range(2, int(math.ceil(math.sqrt(number)))+1, 1):
        if number % j == 0:
            return False
    return True


total_sum = 2


for i in range(1, 2000000, 2):
    if is_prime(i):
        total_sum += i
        print(f"{i}")
print(f"Total Sum: {total_sum}")