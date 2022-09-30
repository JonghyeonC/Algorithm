def dfs(num, k):
    global max_v, min_v
    if k == N:
        if num > max_v:
            max_v = num
        if num < min_v:
            min_v = num
    else:
        for i in range(4):
            if operator_num[i]:
                operator_num[i] -= 1
                if i == 0:
                    dfs(num + num_list[k], k + 1)
                elif i == 1:
                    dfs(num - num_list[k], k + 1)
                elif i == 2:
                    dfs(num * num_list[k], k + 1)
                elif i == 3:
                    dfs(int(num / num_list[k]), k + 1)
                operator_num[i] += 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    operator_num = list(map(int, input().split()))  # 2101
    num_list = list(map(int, input().split()))
    max_v = -1000000000
    min_v = 1000000000
    dfs(num_list[0], 1)
    print(f'#{tc} {max_v - min_v}')