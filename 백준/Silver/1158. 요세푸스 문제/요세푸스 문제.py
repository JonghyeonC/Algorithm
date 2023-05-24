N, K = map(int, input().split())
arr = [i for i in range(1, N + 1)]
result = []
idx = 0
while arr:
    idx = (idx + K - 1) % len(arr)
    tmp = arr.pop(idx)
    result.append(tmp)
print('<', end="")
for i in range(len(result) - 1):
    print(result[i], end='')
    print(',', end=' ')
print(result[-1], end="")
print(">")