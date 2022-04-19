set_1 = set()
set_2 = set()

n = int(input())
n += int(input())
n += int(input())

for i in range(n):
    name = input()
    if not name in set_1:
        set_1.add(name)
    else:
        if not name in set_2:
            set_2.add(name)
        else:
            set_2.remove(name)
print(len(set_2) if set_2 else 'NO')
