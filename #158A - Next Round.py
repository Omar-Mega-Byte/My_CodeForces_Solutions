def P4():
    data = list(map(int, input().split()))  # Read n and k
    n = data[0]
    k = data[1]
    count = 0

    numbers = list(map(int, input().split()))  # Read the scores
    threshold = numbers[k - 1]  # k-th participant's score (1-indexed in input, convert to 0-indexed)

    for number in numbers:
        if number >= threshold and number > 0:
            count += 1

    print(count)
