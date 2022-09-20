bit_table = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
}
rule = {
    '211': 0, '221': 1, '122': 2, '411': 3, '132': 4,
    '231': 5, '114': 6, '312': 7, '213': 8, '112': 9

}


def calcul(a, b, c):
    divider = min(a, b, c)
    a //= divider
    b //= divider
    c //= divider
    text = str(c) + str(b) + str(a)
    return text


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    temp = [input() for _ in range(N)]
    arr = [''] * N
    for i in range(N):
        for j in range(M):
            arr[i] += bit_table[temp[i][j]]
    result = []
    ans = 0
    for i in range(1, N):
        a = b = c = 0
        for j in range(4 * M - 1, -1, -1):
            if b == 0 and c == 0 and arr[i][j] == '1' and arr[i-1][j] == '0':
                a += 1
            elif a > 0 and c == 0 and arr[i][j] == '0' and arr[i-1][j] == '0':
                b += 1
            elif a > 0 and b > 0 and arr[i][j] == '1' and arr[i-1][j] == '0':
                c += 1
            if a > 0 and b > 0 and c > 0 and arr[i][j] == '0' and arr[i-1][j] == '0':
                result.append(rule[calcul(a, b, c)])
                a = b = c = 0
            total = odd = even = 0
            if len(result) == 8:
                result = result[::-1]
                odd = result[0] + result[2] + result[4] + result[6]
                even = result[1] + result[3] + result[5] + result[7]
                total = odd * 3 + even
                if total % 10 == 0:
                    ans += (odd + even)
                result = []
    print(f'#{tc} {ans}')