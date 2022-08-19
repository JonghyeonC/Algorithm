def f(text):
    l = len(text)
    stack = []
    answer = 0
    for i in range(l):
        if text[i] == '(':
            stack.append(text[i])
        elif text[i] == ')':
            if text[i-1] == '(':
                stack.pop()
                if stack:
                    answer += len(stack)
                else:
                    answer = answer
            elif text[i-1] == ')':
                stack.pop()
                answer += 1
    return answer


T = int(input())
for tc in range(1, T+1):
    text = input()
    print(f'#{tc} {f(text)}')