current_digit = 1
last_digit = 1
new_digit = 1  # change
total = 0

while current_digit <= 4000000:
    print(current_digit)
    if (current_digit % 2) == 0:
        total = total + current_digit
    new_digit = current_digit + last_digit  # This part can be a lot better
    last_digit = current_digit
    current_digit = new_digit

print("Total", total)
