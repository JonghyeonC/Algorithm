n = int(input())
arr = list(map(int, input().split()))

cnt = 1
max_val = 1
for i in range(n-1):
    if arr[i] <= arr[i + 1]:
        cnt += 1
        if max_val < cnt:
            max_val = cnt
    else:
        cnt = 1
cnt = 1
for i in range(n-1):
    if arr[i] >= arr[i+1]:
        cnt += 1
        if max_val < cnt:
            max_val = cnt
    else:
        cnt = 1

print(max_val)