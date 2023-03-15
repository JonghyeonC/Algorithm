import sys
from collections import deque


N, M = map(int, sys.stdin.readline().rstrip().split())
check_list = list(map(int, sys.stdin.readline().rstrip().split()))
q = deque(range(1, N + 1))

ans = idx = 0
while idx < M:
    if q[0] == check_list[idx]:
        q.popleft()
        idx += 1
    else:
        temp = q.index(check_list[idx])
        if temp <= len(q) // 2:
            q.rotate(-1)
            ans += 1
        else:
            q.rotate(1)
            ans += 1
print(ans)
