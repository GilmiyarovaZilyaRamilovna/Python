password = input("Введите пароль: ")
conf_password = input("Повторите пароль: ")
if len(password) < 8:
    print("Короткий")
elif conf_password != password:
    print("Различаются")
else:
    print("ОК")
