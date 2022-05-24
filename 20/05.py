data = input()
count = list(map(lambda x: x.lstrip().startswith("#"), data.split("\n"))).count(True)
print(count)#3
