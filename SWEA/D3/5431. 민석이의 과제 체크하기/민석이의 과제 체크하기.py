T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    numbers = []
    ans = []
    for i in range(1, n+1):
        numbers.append(i)
    for num in numbers:
        if num not in arr:
            ans.append(num)
    ans.sort()
    print(f'#{tc} {" ".join(map(str, ans))}')