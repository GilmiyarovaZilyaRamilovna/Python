def print_only_new(message):
    if message not in old_messages:
        print(message)


if __name__ == '__main__':
    old_messages = set()
    while True:
        message = input()
        if message == '':
            break
        print_only_new(message)
        old_messages.add(message)
