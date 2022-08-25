T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    for i in range(N):
        stack = []
        for j in range(N):
            if arr[j][i] == 1:
                if len(stack) == 0:
                    stack.append(arr[j][i])
                elif len(stack) > 0 and stack[-1] == 2:
                    stack.append(arr[j][i])
            elif arr[j][i] == 2:
                if len(stack) > 0 and stack[-1] == 1:
                    stack.append(arr[j][i])
        ans += len(stack) // 2
    print(f'#{tc} {ans}')