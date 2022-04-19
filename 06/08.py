b = set()
a = int(input())
w = int(input())
for f in range(w):
        b.add(input())
for f in range(a - 1) :
    n = set()
    for i in range(int(input())) :
        n.add(input())
    b = b & n
for i in b :
    print(i)