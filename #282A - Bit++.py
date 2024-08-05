x = 0
num = int(input())

for _ in range(num):
    operation = input().strip()
    if "++" in operation:
        x += 1
    elif "--" in operation:
        x -= 1

print(x)
