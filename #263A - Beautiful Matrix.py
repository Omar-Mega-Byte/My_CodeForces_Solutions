def P6():
    numbers = []
    count = 0
    target_col = 2
    target_row = 2
    # Read numbers into the list
    for i in range(5):
        row = list(map(int, input().split()))
        numbers.append(row)
        if 1 in row:
            one_row = i
            one_col = row.index(1)

    count = abs(target_col - one_col) + abs(target_row - one_row)
    print(count)
