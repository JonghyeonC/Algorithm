while True:
    str = input()
    stack = []

    if str == '.':
        break

    for c in str:
        if c == '[' or c == '(':
            stack.append(c)
        elif c == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(c)
                break
        elif c == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(c)
                break

    if len(stack) == 0:
        print('yes')
    else:
        print('no')