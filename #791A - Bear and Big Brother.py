text = list(map(int, input().split()))
Limak_Age = int(text[0])
Bob_Age = int(text[1])
count = 0
while not (Limak_Age > Bob_Age):
    Limak_Age = Limak_Age * 3
    Bob_Age = Bob_Age * 2
    count += 1

print(count)
