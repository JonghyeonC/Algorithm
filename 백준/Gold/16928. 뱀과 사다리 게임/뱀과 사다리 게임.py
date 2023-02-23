from collections import deque


def bfs():
    q = deque([1])
    visited[1] = 1
    while q:
        x = q.popleft()
        if x == 100:
            return
        for dice in range(1, 7):
            next_loca = x + dice
            if 1 <= next_loca <= 100 and visited[next_loca] == 0:
                if next_loca in ladder:
                    next_loca = ladder[next_loca]
                if visited[next_loca] == 0:
                    visited[next_loca] = 1
                    boards[next_loca] = boards[x] + 1
                    q.append(next_loca)


N, M = map(int, input().split())
boards = [0] * 101
visited = [0] * 101
ladder = {}
for _ in range(N + M):
    a, b = map(int, input().split())
    ladder[a] = b
bfs()
print(boards[100])
