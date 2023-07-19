from collections import deque
N, K = map(int, input().split())
arr = deque([i for i in range(1, N + 1)])
ans = []
while arr:
    arr.rotate(-(K - 1))
    ans.append(arr.popleft())
print('<', end='')
for i in range(N - 1):
    print(ans[i], end="")
    print(',', end=' ')
print(f'{ans[-1]}>')
