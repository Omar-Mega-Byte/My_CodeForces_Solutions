text = list(map(int, input().split()))
for i in range(text[1]):
    last_digit = text[0] % 10
    if last_digit != 0:
        text[0] = text[0] - 1
    else:
        text[0] = text[0] // 10

print(text[0])
