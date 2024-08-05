text = input()
vowels = ['A', 'O', 'Y', 'U', 'I', 'E', 'a', 'o', 'y', 'u', 'i', 'e']
output = []
for letter in text:
    if letter not in vowels:
        output.append(letter)

print('.' + '.'.join(output).lower())
