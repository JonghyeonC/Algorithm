from collections import deque


N = int(input())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

check_a = deque()
check_b = sorted(arr_b, reverse=True)

arr_a.sort()
for num in arr_a:
    check_a.append(num)

new_a = [-1] * N

for num in check_b:
    for i in range(N):
        if num == arr_b[i] and new_a[i] == -1:
            new_a[i] = check_a.popleft()

ans = 0
for i in range(N):
    ans += arr_b[i] * new_a[i]
print(ans)