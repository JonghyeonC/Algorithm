T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    ans = -1
    num = 0
    for i in range(n):
        for j in range(i+1, n):
            num = arr[i] * arr[j]
            flag = 1
            for k in range(len(str(num))-1):
                if int(str(num)[k]) > int(str(num)[k+1]):
                    flag = 0
                    break
            if flag == 1:
                if num > ans:
                    ans = num

    print(f'#{tc} {ans}')