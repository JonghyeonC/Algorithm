N = int(input())
arr = list(map(int, input().split()))
box = [1] * N

for i in range(1, N):
    tmp = 0
    for j in range(i - 1, -1, -1):
        if arr[i] > arr[j]:
            tmp = max(tmp, box[j])
    box[i] += tmp
print(max(box))
