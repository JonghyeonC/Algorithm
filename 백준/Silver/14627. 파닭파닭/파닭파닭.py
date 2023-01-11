import sys
input = sys.stdin.readline
S, C = map(int, input().split())

sp = []
for _ in range(S):
    sp.append(int(input()))

start = 1
end = max(sp)
ans = 0
while start <= end:
    cnt = 0
    mid = (start + end) // 2

    for num in sp:
        cnt += num // mid

    if cnt >= C:
        start = mid + 1
        ans = max(mid, ans)
    else:
        end = mid - 1

print(sum(sp) - C * ans)
