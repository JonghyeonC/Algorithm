rule = [
    '0001101', '0011001', '0010011', '0111101', '0100011',
    '0110001', '0101111', '0111011', '0110111', '0001011'
]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]

    code = []
    flag = 0
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == 1:
                code.append(arr[i][j-55:j+1])
                flag = 1
                break
        if flag:
            break
    check = []
    for i in range(0, 56, 7):
        check.append(code[0][i:i+7])
    codes = []
    for num in check:
        codes.append(''.join(map(str, num)))

    result = []
    for i in range(len(codes)):
        for j in range(len(rule)):
            if codes[i] == rule[j]:
                result.append(j)

    odd = even = 0
    for i in range(len(result)):
        if (i + 1) % 2 == 1:
            odd += result[i]
        else:
            even += result[i]
    if (odd * 3 + even) % 10 == 0:
        print(f'#{tc} {odd + even}')
    else:
        print(f'#{tc} 0')