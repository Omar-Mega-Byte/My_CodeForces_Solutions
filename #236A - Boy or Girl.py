def P10():
    text = input().strip()
    letters = []
    count = 0
    for letter in text:
        if letter not in letters:
            letters.append(letter)
            count += 1

    if count % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")
