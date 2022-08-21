T = int(input())
for tc in range(1, T+1):
    num = int(input())
    arr = [2, 3, 5, 7, 11]
    answer = [0] * 5
    while num > 1:
        for i in range(len(arr)):
            if num % arr[i] == 0:
                answer[i] += 1
                num /= arr[i]

    print(f'#{tc}', end=' ')
    for i in answer:
        print(i, end=' ')
    print()