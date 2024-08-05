def P2():
    num = int(input())
    numbers = []

    # Read numbers into the list
    for _ in range(num):
        row = list(map(int, input().split()))
        numbers.append(row)

    count = 0

    for number in numbers:
        if sum(number) >= 2:
            count += 1

    print(count)
