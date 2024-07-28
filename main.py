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
