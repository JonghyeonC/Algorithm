N, M = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
start = 0
end = 0
while start <= N and end <= N:
    total = sum(arr[start:end])
    if total < M:
        end += 1
    elif total > M:
        start += 1
    elif total == M:
        cnt += 1
        end += 1
print(cnt)