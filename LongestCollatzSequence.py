import math
max_value = 999999


def collatz(number):
    if (number % 2) == 0:
        return number/2
    else:
        return (number * 3) + 1


def collatz_sequence(number):
    count = 1
    while number != 1:
        number = collatz(number)
        count += 1
    return count


largest_sequence = [0, 0]  # Number, Terms

for i in range(max_value, 1, -1):
    current_sequence = collatz_sequence(i)
    if current_sequence > largest_sequence[1]:
        largest_sequence[1] = current_sequence
        largest_sequence[0] = i

print(f"Largest Sequence is: {largest_sequence[1]}")
print(f"Collatz Number is: {largest_sequence[0]}")
