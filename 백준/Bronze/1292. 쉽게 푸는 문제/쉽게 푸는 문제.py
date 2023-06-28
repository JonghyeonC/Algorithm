start, end = map(int, input().split())
arr = []
for i in range(1, end + 1):
    for _ in range(1, i + 1):
        arr.append(i)
ans = sum(arr[start - 1:end])
print(ans)