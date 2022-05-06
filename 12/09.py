dct = {}
for sumb in input():
    if sumb.isalpha():
        sumb = sumb.lower()
        dct[sumb] = dct.get(sumb,0)+1
print(max(sorted(dct),key = lambda x : dct[x]))
