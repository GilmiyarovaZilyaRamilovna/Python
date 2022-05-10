eng = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'i', 'k', 'l', 'm', 'n',
       'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'tc', 'ch', 'sh', 'shch', '',
       'y', '', 'e', 'iu', 'ia']
trans = {}
for i in range(1072, 1103 + 1):
    trans[chr(i)] = eng[i - 1072]
for i in input():
    if 1040 <= ord(i) <= 1103:
        if i.isupper():
            print(trans[i.lower()].capitalize(), end='')
        else:
            print(trans[i], end='')
    elif ord(i) in [1025, 1105]:
        if i.isupper():
            print('E', end='')
        else:
            print('e', end='')
    else:
        print(i, end='')