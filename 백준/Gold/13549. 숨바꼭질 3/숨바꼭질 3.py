from collections import deque


def f(x):
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        if x == end:
            return
        else:
            for n_x in (2 * x, x - 1, x + 1):
                if 0 <= n_x <= 100000 and visited[n_x] == 0:
                    if n_x == 2 * x:
                        q.append(n_x)
                        visited[n_x] = visited[x]
                    else:
                        q.append(n_x)
                        visited[n_x] = visited[x] + 1


start, end = map(int, input().split())
visited = [0] * 100001
f(start)
print(visited[end])