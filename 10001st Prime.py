prime_count = 1
check_this_number = 1


def is_prime(number):
    if number == 1:
        return False
    for j in range(2, number, 1):
        if number % j == 0:
            return False
    return True


while prime_count < 10001:
    print(f"Prime Count: {prime_count}")
    if is_prime(check_this_number):
        prime_count += 1
    check_this_number += 2


print(f"The 10000st Prime is {check_this_number - 2}")
