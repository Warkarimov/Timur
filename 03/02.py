password_1 = input()
password_2 = input()
if len(password_1) < 8:
    print('Короткий')
elif password_1 != password_2:
    print('Различаются')
else:
    print('OK')