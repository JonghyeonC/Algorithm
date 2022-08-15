t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    total = 0
    answer = 0
    max_idx = n-1
    for i in range(n-2, -1, -1):
        if arr[max_idx] > arr[i]:
            total += arr[i]
            cnt += 1
        elif arr[max_idx] == arr[i]:
            continue
        elif arr[max_idx] < arr[i]:
            answer += arr[max_idx] * cnt - total
            max_idx = i
            cnt = 0
            total = 0

    answer += arr[max_idx] * cnt - total

    print(f'#{tc} {answer}')