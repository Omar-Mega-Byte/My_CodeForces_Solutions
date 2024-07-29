#######################################################################

# A. Way Too Long Words
def P1():
    num = int(input())
    text = []

    # Read words into the list
    for _ in range(num):
        text.append(input().strip())

    # Process each word and print the result
    for word in text:
        if len(word) > 10:
            print(word[0] + str(len(word) - 2) + word[-1])
        elif len(word) <= num or (num < len(word) <= 10):
            print(word)


#######################################################################

# B. A Team
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


#######################################################################

# C. Bit++
def P3():
    x = 0
    num = int(input())

    for _ in range(num):
        operation = input().strip()
        if "++" in operation:
            x += 1
        elif "--" in operation:
            x -= 1

    print(x)


#######################################################################

# D. Next Round

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


#######################################################################

# E. Domino piling
def P5():
    data = list(map(int, input().split()))  # Read n and k
    n = data[0]
    k = data[1]
    mul = n * k
    print(mul // 2)


#######################################################################

# F. Beautiful Matrix

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


#######################################################################

# G. Petya and Strings

def P7():
    text1 = input().strip()
    text2 = input().strip()

    text1 = text1.lower()
    text2 = text2.lower()

    if text1 < text2:
        print(-1)
    elif text1 > text2:
        print(1)
    else:
        print(0)

#######################################################################
