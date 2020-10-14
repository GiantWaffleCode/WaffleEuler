#largest = 998001

# 997799

y = 999
largest_product = 0
x_l = 0
y_l = 0

for x in range(9999, 9899, -1):
    for y in range(9999, 899, -1):
        product = x * y
        number_string = f"{product}"
        number_reversed = number_string[::-1]
        if product - int(number_reversed) == 0:
            if product > largest_product:
                largest_product = product
                x_l = x
                y_l = y
print(f"The Largest Palindrome is:{largest_product}")
print(f"Its multiples are: {x_l} and {y_l}")





