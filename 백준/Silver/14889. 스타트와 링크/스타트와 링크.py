import copy


def comb(k, s):
    result_2 = []
    if k == N // 2:
        for i in n:
            if i not in result_1:
                result_2.append(i)
        a_1 = copy.deepcopy(result_1)
        a_2 = result_2
        ans_1.append(a_1)
        ans_2.append(a_2)
    else:
        for i in range(s, N):
            result_1[k] = n[i]
            comb(k + 1, i + 1)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
n_arr = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        n_arr[j][i] = n_arr[i][j] = arr[i][j] + arr[j][i]
result_1 = [0] * (N // 2)
ans_1 = []
ans_2 = []
n = [i for i in range(N)]
comb(0, 0)
min_v = 987654321
for i in range(len(ans_1)):
    temp_1 = 0
    temp_2 = 0
    for x in range(len(ans_1[0]) - 1):
        for y in range(x + 1, len(ans_1[0])):
            temp_1 += n_arr[ans_1[i][x]][ans_1[i][y]]
            temp_2 += n_arr[ans_2[i][x]][ans_2[i][y]]
    ans = abs(temp_1 - temp_2)
    min_v = min(ans, min_v)
print(min_v)