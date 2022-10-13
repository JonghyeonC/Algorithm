T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    number = list(input())
    num_set = set()
    num_list = []
    for _ in range(N // 4):
        for i in range(0, N, N // 4):
            ans = number[i:i + N // 4]
            num_set.add(''.join(ans))
        last = number.pop()
        number.insert(0, last)
    for temp in num_set:
        num = int(temp, 16)
        num_list.append(num)
    num_list.sort(reverse=True)
    print(f'#{tc} {num_list[K - 1]}')