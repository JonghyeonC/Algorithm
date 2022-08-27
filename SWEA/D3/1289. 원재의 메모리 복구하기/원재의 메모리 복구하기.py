T = int(input())
for tc in range(1,T+1):
    text = input()

    stack = []
    cnt = 0
    for i in range(len(text)):
        if len(stack) == 0 and text[i] == '1':
            stack.append(text[i])
            cnt += 1
        elif len(stack) == 0 and text[i] == '0':
            stack.append(text[i])
        elif stack[-1] != text[i]:
            cnt += 1
            stack.append(text[i])
    print(f'#{tc} {cnt}')