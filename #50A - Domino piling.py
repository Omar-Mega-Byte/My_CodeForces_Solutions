def P5():
    data = list(map(int, input().split()))  # Read n and k
    n = data[0]
    k = data[1]
    mul = n * k
    print(mul // 2)
