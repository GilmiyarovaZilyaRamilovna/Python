def whoAreYouAndHello():
    x = input()
    while (x.isalpha() and x[0].isupper()) == False:
        x = input()
    print('Привет, {}!'.format(x))


whoAreYouAndHello()