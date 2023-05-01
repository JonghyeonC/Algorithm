N = int(input())
visited = [0] * 101
people = list(map(int, input().split()))
ans = 0
for each in people:
    if visited[each] == 0:
        visited[each] = 1
    else:
        ans += 1
print(ans)