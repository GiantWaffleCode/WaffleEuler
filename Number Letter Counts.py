def convert_num_to_string(input_number):
    d = {
        0: 0,
        1: len("one"),
        2: len("two"),
        3: len("three"),
        4: len("four"),
        5: len("five"),
        6: len("six"),
        7: len("seven"),
        8: len("eight"),
        9: len("nine"),
        10: len("ten"),
        11: len("eleven"),
        12: len("twelve"),
        13: len("thirteen"),
        14: len("fourteen"),
        15: len("fifteen"),
        16: len("sixteen"),
        17: len("seventeen"),
        18: len("eighteen"),
        19: len("nineteen"),
        20: len("twenty"),
        30: len("thirty"),
        40: len("forty"),
        50: len("fifty"),
        60: len("sixty"),
        70: len("seventy"),
        80: len("eighty"),
        90: len("ninety"),
        100: len("hundred"),
        1000: len("thousand")
    }

    number_total = 0

    if input_number == 1000:
        return 11
    if 1000 > input_number >= 100:
        if input_number % 100 == 0:
            return d[int(str(input_number)[-3])] + d[100]
        number_total += d[int(str(input_number)[-3])] + d[100] + 3
        if 19 >= int(str(input_number)[-2:]) > 10:
            number_total += d[int(str(input_number)[-2:])]
            return number_total
        else:
            number_total += d[int(str(input_number)[-2]) * 10]
            number_total += d[int(str(input_number)[-1])]
            return number_total
    if 100 > input_number > 20:
        number_total += d[int(str(input_number)[-2]) * 10]
        number_total += d[int(str(input_number)[-1])]
        return number_total
    if 20 >= input_number >= 10:
        number_total += d[int(str(input_number)[-2:])]
        return number_total
    else:
        number_total += d[int(str(input_number)[-1])]
        return number_total


total_sum = 0
temp_sum = 0

for i in range(1, 1001, 1):
    temp_sum = convert_num_to_string(i)
    print(i, temp_sum)
    total_sum += temp_sum
print(f"The Total is:{total_sum}")

