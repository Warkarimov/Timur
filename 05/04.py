n = int(input())
for i in range(n):
    word = input()
    if 'Кот' in word or 'кот' in word:
        print('КОТ')
        break
else:
    print('НЕТ')