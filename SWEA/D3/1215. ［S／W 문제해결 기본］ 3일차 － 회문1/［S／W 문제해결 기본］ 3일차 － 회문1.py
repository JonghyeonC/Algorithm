def palindrome(arr, n):
    r = 8
    cnt = 0
    for i in range(r):
        for j in range(r - n + 1):
            flag = 1
            for k in range(n//2):
                if arr[i][j + k] != arr[i][j + n - 1 - k]:
                    flag = 0
            if flag == 1:
                cnt += 1

    for i in range(r):
        for j in range(r - n + 1):
            flag = 1
            for k in range(n//2):
                if arr[j + k][i] != arr[j + n - k - 1][i]:
                    flag = 0
            if flag == 1:
                cnt += 1
    return cnt


T = 10
for tc in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(8)]

    print(f'#{tc} {palindrome(arr, n)}')