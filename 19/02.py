def simple_map(transformation, values):
    return [transformation(x) for x in values]

values = [1, 3, 1, 5, 7]
print(*simple_map(lambda x: x + 5, values))


