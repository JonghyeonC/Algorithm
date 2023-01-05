from collections import deque


N = int(input())
arr_a = list(map(int, input().split()))   # 배열 A
arr_b = list(map(int, input().split()))   # 배열 B

check_a = deque()                         # 계속해서 pop을 해야하기 때문에 deque로 만들어줌
check_b = sorted(arr_b, reverse=True)     # 배열 B를 수정하지 않고 새롭게 내림차순으로 정렬

arr_a.sort()                              # 배열 A를 오름차순으로 정렬
for num in arr_a:
    check_a.append(num)                   # 배열 A의 값을 deque로 만든 배열 A 대용에 넣어줌

new_a = [-1] * N                          # 새로운 배열의 크기를 최대값으로 초기화

for num in check_b:                       # 따로 정렬시킨 배열 B의 값을 하나씩 진짜 배열 B랑 비교
    for i in range(N):
        if num == arr_b[i] and new_a[i] == -1:  # 진짜 배열 B와 같으면서 아직 해당 위치에 새로운 값을 넣은 적이 없다면
            new_a[i] = check_a.popleft()  # 새로운 배열 A에 배열 A의 가장 작은 값부터 넣어줌
# 배열 B의 가장 큰 값에 배열 A의 가장 작은 값을 연결시켜서 최소값을 구하는 것이 목적
ans = 0
for i in range(N):
    ans += arr_b[i] * new_a[i]
print(ans)
