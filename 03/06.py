while True:
    password_1 = input()
    if len(password_1) < 8:
        print('Короткий')
    elif '123' in password_1:
        print('Простой!')
    else:
        password_2 = input()
        if password_1 != password_2:
            print('Различаются.')
        else:
            print('OK')