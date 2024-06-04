a = int(input('Введите рост 1-го мальчика: '))
b = int(input('Введите рост 2-го мальчика: '))
c = int(input('Введите рост 3-го мальчика: '))

if a < b < c:
    low = a
    mid = b
    high = c
elif a < c < b:
    low = a
    mid = c
    high = b
else:
    if b < c < a:
        low = b
        mid = c
        high = a
    elif b < a < c:
        low = b
        mid = a
        high = c
    else:
        if c < a < b:
            low = c
            mid = a
            high = b
        elif c < b < a:
            low = c
            mid = b
            high = a
print(high)