value = str(2**500)
value_sum = 0

for i in range(0, len(value), 1):
    value_sum += int(value[i])
print(value_sum)
