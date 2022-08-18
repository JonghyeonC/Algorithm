n, k = map(int, input().split())
arr = list(map(int, input().split()))

total = []
total.append(sum(arr[:k]))

for i in range(n-k):
    total.append(total[i] - arr[i] + arr[i+k])
answer = max(total)

print(answer)