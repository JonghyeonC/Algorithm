from collections import deque
N = int(input())
arr = deque()
for i in range(1, N + 1):
    arr.append(i)
while len(arr) >= 2:
    arr.popleft()
    a = arr.popleft()
    arr.append(a)
print(*arr)