import sys
input = sys.stdin.readline


N = int(input())
arr = []
result = [[0] * 3 for _ in range(N)]
for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(N):
    for j in range(3):
        if i == 0:
            result[i][j] = arr[i][j]
        else:
            result[i][j] = min(result[i - 1][(j + 1) % 3], result[i - 1][(j + 2) % 3]) + arr[i][j]
print(min(result[-1]))