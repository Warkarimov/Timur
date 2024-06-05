count = 0
while True:
    count += 1
    word = input()
    if 'Кот' in word or 'кот' in word:
        print(count)
        break
    elif 'СТОП' in word:
        print(-1)
