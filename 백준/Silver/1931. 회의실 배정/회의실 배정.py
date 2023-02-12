N = int(input())
arr = []
for _ in range(N):
    s, e = map(int, input().split())
    arr.append([s, e])
rooms = sorted(arr, key=lambda x: (x[1], x[0]))
ans = 1
end = rooms[0][1]
i = 1
while i <= N - 1:
    if rooms[i][0] >= end:
        ans += 1
        end = rooms[i][1]
    i += 1
print(ans)