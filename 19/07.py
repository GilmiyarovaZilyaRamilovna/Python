def same_by(characteristic, objects):
    result, result1 = [], []
    for i in objects:
        if characteristic(i) == 0:
            result.append(i)
        else:
            result1.append(i)
    if result == objects or result1 == objects:
        return True
    return False

values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
