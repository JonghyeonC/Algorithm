# 트리의 지름이라는 임의의 정점에서 가장 멀리 있는 곳에서 가장 멀리 있는 곳까지의 거리를 말함
# https://blog.myungwoo.kr/112 참고할 것
import sys
def dfs(x, visited):
    for node, dist in tree[x]:
        if visited[node] == 0:
            visited[node] = visited[x] + dist
            dfs(node, visited)


N = int(input())
tree = [[] for _ in range(N + 1)]                    # 트리의 노드를 입력받기 위한 배열
visited_1 = [0] * (N + 1)                            # 첫 번째 임의의 점에서 먼 거리를 구하기 위한 방문 배열
visited_2 = [0] * (N + 1)                            # 처음 가장 먼 거리에서 먼 거리를 구하기 위한 방문 배열
for _ in range(N):                         
    arr = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(arr) - 1, 2):            
        tree[arr[0]].append((arr[i], arr[i + 1]))    # 2개씩 입력받기 위함
        
visited_1[1] = 1
dfs(1, visited_1)                                    # 임의의 정점을 1로 설정하고, dfs를 실행
                                     # 양방향이므로 시작위치를 

max_idx = visited_1.index(max(visited_1))
visited_2[max_idx] = 1
dfs(max_idx, visited_2)

print(max(visited_2) - 1)