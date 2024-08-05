def P8():
    text = input().strip()
    split_numbers = text.split('+')

    int_nums = [int(num) for num in split_numbers]

    sorted_nums = sorted(int_nums)

    str_nums = [str(num) for num in sorted_nums]

    print('+'.join(str_nums))
