print("Вы видите перед собой "
      " 3 двери. Первая с цветочками, вторая с бабочками, и третья со звездочками . Какую выберите?")
answer1 = input("Укажите какую вы виберите? (\"с цветочками\", \"с бабочками\" или \"со звездочками\"): ")
if answer1.lower() == "с цветочками":
    print("Войдя в комнату, вы оказываетесь на цветочном лугу.")
elif answer1.lower() == "с бабочками":
    print("Войдя в комнату, вы оказываетесь в поле, где тетают много бабочек.")
elif answer1.lower() == "со звездочками":
    answer2 = input("Войдя в комнату вы видите 2 двери. В какую вы пойдете? (\"левый\" или \"правый \"): ")
    if answer2.lower() == "правый":
        print("Войдя, вы окажетесь в космосе среди звезд")
    elif answer2.lower() == "левый":
        print("Войдя, вы оказываетесь в подводном мире.")
    else:
        print("Ошибка")
else:
    print("Ошибка")
