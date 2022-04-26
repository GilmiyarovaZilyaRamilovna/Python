n = int(input())

for i in range(n):
    s = input()
    if '%%' in s[:2]:
        print(s[2:])
    elif '####' in s[:4]:
        continue
    else:
        print(s)