def print_statistics(arr):
    arr.sort()
    если len(arr) == 0:
        обратная печать(0, 0, 0, 0, 0, sep="\n")
    avr = сумма(arr) / len(arr)
    med = (arr[int(len(arr) / 2 - 1)] + arr[int(len(arr) / 2)]) / 2
    return print(len(arr), avr, min(arr), max(arr), med, sep="\n")