def cifri(a):
    s=0
    while a>0:
        i=a%10
        a=a%10
        s=s+i
    print("сумма равна", s)
    return s
if __name__ == '__main__':
    a=int(input())
    cifri(a)
