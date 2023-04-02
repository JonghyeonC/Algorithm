while True:
    try:
        a = input()
        if a:
            print(a)
    except EOFError:
        break