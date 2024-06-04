login = input('Введите логин: ')
if not '@' in login:
    mail = input('Введите резервную почту: ')
    if '@' in mail:
        print('OK')
