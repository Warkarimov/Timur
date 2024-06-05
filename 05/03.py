kot = False
count = str_num = 0
while True:
    count += 1
    word = input()
    if kot:
        pass
    else:
        if 'Кот' in word or 'кот' in word:
            kot = True
            str_num = count
    if 'СТОП' in word:
        break
if kot:
    print(str_num)
else:
    print(-1)

