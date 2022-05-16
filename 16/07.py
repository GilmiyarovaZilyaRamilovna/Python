persons = {}
last_person = ""


def setup_profile(name, vacation_dates):
    global last_person
    persons[name] = vacation_dates
    last_person = name


def print_application_for_leave():
    print(f"Заявление на отпуск в период {persons[last_person]}. {last_person}")


def print_holiday_money_claim(amount):
    print(f"Прошу выплатить {amount} отпускных денег. {last_person}")


def print_attorney_letter(to_whom):
    print(f"На время отпуска в период {persons[last_person]} "
          f"моим заместителем назначается {to_whom}. {last_person}")

    setup_profile("Иван Петров", "1 июня – 20 июня")
    print_application_for_leave()
    print_application_for_leave()
    print_holiday_money_claim("15 тысяч пиастров")
    print_attorney_letter("Василий Васильев")
