n = int(input())
res = []
for _ in range(n):
    tmp = any([int(input()[-1]) == 5 for _ in range(int(input()))])
    res.append(tmp)

if all(res):
    print('ДА')
else:
    print('НЕТ')