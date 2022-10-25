def dfs(ssum, k):
    global max_v, min_v
    if k == N:
        if max_v < ssum:
            max_v = ssum
        if min_v > ssum:
            min_v = ssum
    else:
        for i in range(4):
            if syms[i]:
                syms[i] -= 1
                if i == 0:
                    dfs(ssum + numbers[k], k + 1)
                elif i == 1:
                    dfs(ssum - numbers[k], k + 1)
                elif i == 2:
                    dfs(ssum * numbers[k], k + 1)
                elif i == 3:
                    dfs(int(ssum / numbers[k]), k + 1)
                syms[i] += 1


N = int(input())
numbers = list(map(int, input().split()))
syms = list(map(int, input().split()))
max_v = -987654321
min_v = 987654321

dfs(numbers[0], 1)
print(max_v)
print(min_v)