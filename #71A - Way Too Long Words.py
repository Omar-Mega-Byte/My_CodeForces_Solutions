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
