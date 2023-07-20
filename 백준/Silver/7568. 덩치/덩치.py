N = int(input())
arr = []
ans = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))
for t_x, t_y in arr:
    tmp = 0
    for x, y in arr:
        if t_x < x and t_y < y:
            tmp += 1
    ans.append(tmp + 1)
print(*ans)