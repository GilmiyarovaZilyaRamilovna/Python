a = list()
b = int(input())
for i in range(b):
    c = input()
    if 'Не' in c[0:3] or 'не' in c[0:3]:
        if 'нечего' not in c and 'Нестояние' not in c:
            c = c[3:]
    print(c)
for i in a:
    print(i)