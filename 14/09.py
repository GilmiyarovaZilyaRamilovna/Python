def ask_password():
    for i in range(0, 3):
        s = input()
        if s == 'password':
            print('Пароль принят')
            break
        if i == 2:
            print("В доступе отказано")
