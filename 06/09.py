hi = int(input())
sp1 = set()
sp2 = set()
for i in range(hi):
    im = input()
    if im in sp1:
        sp2.add(im)
    else:
        sp1.add(im)
rez = sp1 - sp2
raz = hi - len(rez)
print(raz)