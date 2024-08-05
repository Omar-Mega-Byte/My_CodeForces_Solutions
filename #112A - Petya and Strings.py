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
