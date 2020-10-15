import math

not_found = True
check_number = 20

while not_found:
    for i in range(20, 10, -1):
        if check_number % i != 0:
            check_number += 20
            break
        if i == 11:
            not_found = False
            print(f"Smallest Value: {check_number}")
            quit()

