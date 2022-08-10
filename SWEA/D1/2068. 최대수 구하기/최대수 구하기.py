num = int(input())
for tc in range(1, num+1):
    numbers = list(map(int, input().split()))
    ans = numbers[0]
    for i in numbers:
        if i > ans:
            ans = i
    print(f'#{tc} {ans}')