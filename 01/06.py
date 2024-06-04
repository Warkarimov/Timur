question1 = input('Любите ли вы котиков?: ')
if question1 != 'Да' and question1 != 'Нет':
    print('Ошибка')
    exit()
question2 = input('Умеете ли вы программировать?: ')
if question2 != 'Да' and question2 != 'Нет':
    print('Ошибка')
    exit()
else:
    if 'Да' in question1 and 'Да' in question2:
        print('Вы обладаете незаурядным умом.')
    elif 'Нет' in question1 and 'Нет' in question2:
        print('Вы не обладаете незаурядным умом.')
    elif 'Да' in question1 and 'Нет' in question2:
        print('Вы любите котиков<3, но не умеете программировать')
    elif 'Нет' in question1 and 'Да' in question2:
        print('Вы не любите котиков(((. Но за то умеете программировать...')