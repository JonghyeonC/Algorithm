num = int(input())
for tc in range(1, num+1):
    a, b = map(int, input().split())
    if a > b:
        print(f'#{tc} >')
    elif a == b:
        print(f'#{tc} =')
    else:
        print(f'#{tc} <')