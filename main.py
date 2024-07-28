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
        elif len(word) <= num or (len(word) > num and len(word) <= 10):
            print(word)


#######################################################################

# B. A Team
num = int(input())
numbers = []  # Initialize an empty list to hold the sublist

# Read numbers into the list
for _ in range(num):
    row = []  # Create a new list for each row
    for i in range(3):
        row.append(int(input()))
    numbers.append(row)  # Add the row to the numbers list

count = 0

for number in range(num):
    for i in range(2):
        if numbers[number][i] == numbers[number][i + 1] or numbers[number][i] == numbers[number][i + 2] or \
                numbers[number][i] == numbers[number][i + 2] == numbers[number][i + 1]:
            count += 1
    return count

# print(numbers)
