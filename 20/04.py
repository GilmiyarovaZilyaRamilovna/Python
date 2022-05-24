s, k = 0, 0

while True:
    try:
        s += float(input())
        k += 1
    except ValueError:
        break

print(-1 if not s else s / k)
