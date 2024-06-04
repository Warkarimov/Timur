a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = input('Какую операцию провести с числами?: ')
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '/':
    if b == 0:
        print(888888)
    else:
        print(a / c)
elif c == '*':
    print(a * b)
else:
    print(888888)
