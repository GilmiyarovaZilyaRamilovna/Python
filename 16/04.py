products = {}
numeration = 1
index_count = 0


def add_item(item_name, item_cost):
    global index_count
    products[index_count] = {item_name: item_cost}
    index_count += 1


def print_receipt():
    global numeration, products
    final_cost = 0
    if products:
        print(f"Чек {numeration}. Всего предметов: {len(products)}")
        for item in products.values():
            name, cost = list(item.items())[0]
            print(f"{name} - {cost}")
            final_cost += cost
        print(f"Итого: {final_cost}\n-----")
        numeration += 1
        products = {}

        add_item('Блокнот', 100)
        print_receipt()

        add_item('Ручка', 70)
        print_receipt()
        print_receipt()

        add_item('Булочка', 15)
        add_item('Булочка', 15)
        add_item('Чай', 5)
        print_receipt()

        add_item('Булочка', 15)
        add_item('Булочка', 15)
        # (Отменить чек) - этот чек не печатаем
