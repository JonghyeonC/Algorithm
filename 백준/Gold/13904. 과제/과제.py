arr = []
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])

arr.sort(reverse=True, key=lambda x : x[1])
result = [0] * 1000
for i in range(N):
    for j in range(arr[i][0] - 1, -1, -1):
        if result[j] == 0:
            result[j] = arr[i][1]
            break
        else:
            continue
print(sum(result))