N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

same = [[0] * N for _ in range(N)]

for j in range(5):
    for i in range(N):
        for k in range(i + 1, N):
            if arr[i][j] == arr[k][j]:
                same[i][k] = 1
                same[k][i] = 1
result = []
for s in same:
    result.append(s.count(1))
print(result.index(max(result)) + 1)