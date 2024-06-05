n = int(input())
kot = False
for i in range(n):
    word = input()
    if 'Кот' in word or 'кот' in word:
        kot = True
if kot:
    print('МЯУ')
else:
    print('Нет')