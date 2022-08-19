def check(arr, n):
    for i in range(n):
        if arr[i] == '(' or arr[i] == '[' or arr[i] == '{' or arr[i] == '<':
            stack.append(arr[i])
        elif arr[i] == ')':
            if len(stack) == 0:
                return 0
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return 0
        elif arr[i] == ']':
            if len(stack) == 0:
                return 0
            else:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return 0
        elif arr[i] == '}':
            if len(stack) == 0:
                return 0
            else:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return 0
        elif arr[i] == '>':
            if len(stack) == 0:
                return 0
            else:
                if stack[-1] == '<':
                    stack.pop()
                else:
                    return 0
    if stack:
        return 0
    else:
        return 1


T = 10
for tc in range(1, T + 1):
    n = int(input())
    arr = list(input())
    stack = []

    print(f'#{tc} {check(arr, n)}')