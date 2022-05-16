def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def larger_root(p, q):
    D = discriminant(1, p, q)
    if D > 0:
        return (-p + D ** 0.5) / 2


def smaller_root(p, q):
    D = discriminant(1, p, q)
    if D > 0:
        return (-p - D ** 0.5) / 2


def main():
    p = float(input())
    q = float(input())
    print(discriminant(1, p, q))
    print(smaller_root(p, q), larger_root(p, q))


print(discriminant(1, 2, 1))
print(smaller_root(3, 1))
print(larger_root(3, 1))
main()
