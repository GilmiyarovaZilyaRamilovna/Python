answer1 = input("Любите смотреть фильмы? ")
answer2 = input("Нравятся мульфильмы? ")
if answer2.lower() == "нет" and answer1.lower() == "нет":
    print("Жаль")
elif answer1.lower() == "нет" and answer2.lower() == "да":
    print("Мне тоже нравятся")
elif answer2.lower() == "нет" and answer1.lower() == "да":
    print("А мне вот нравятся))")
elif answer1.lower() == "да" and answer2.lower() == "да":
    print("Круто! Посмотрим что нибудь интересное?))")
else:
    print("Ошибка. Укажите \"Да\" или \"Нет\".")









