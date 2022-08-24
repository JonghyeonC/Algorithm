T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(str, input().split()))

    ans = []
    if n % 2 == 0:
        left = arr[:n//2]
        right = arr[n//2:]
    elif n % 2 == 1:
        left = arr[:n//2 + 1]
        right = arr[n//2 + 1:]

    for i in range(len(left)):
        ans.insert(0 + 2 * i, left[i])
    for j in range(len(right)):
        ans.insert(1 + 2 * j, right[j])

    print(f'#{tc} {" ".join(ans)}')