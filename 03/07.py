a = 0
b = 1000
c = (a + b) / 2
count = 1
print('Загадайте число от 1 до 1000')
while count < 11:
    count += 1
    x = input('Ваше число ' + str(int(c)) + '? ')
    if x == '>':
        a = c
        c = (a + b) / 2
    elif x == '<':
        b = c
        c = (a + b) / 2
    else:
        print('Ваше число', int(c))
        break
else:
    print('Эх... Не повезло(')