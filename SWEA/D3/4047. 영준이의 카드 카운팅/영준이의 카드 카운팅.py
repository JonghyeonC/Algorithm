def divide(lst, n):
    return [lst[i:i+n] for i in range(0,len(lst), n)]


T = int(input())
for tc in range(1, T+1):
    text = input()
    sen = list(divide(text, 3))

    arr = [0, 0, 0, 0]
    ans = 0
    for i in range(len(sen)):
        for j in range(i+1, len(sen)):
            if sen[i] == sen[j]:
                ans = 'ERROR'
                break
    if ans != 'ERROR':
        for i in range(len(sen)):
            if sen[i][0] == 'S':
                arr[0] += 1
            elif sen[i][0] == 'D':
                arr[1] += 1
            elif sen[i][0] == 'H':
                arr[2] += 1
            else:
                arr[3] += 1
    if ans == 'ERROR':
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} {13-arr[0]} {13-arr[1]} {13-arr[2]} {13-arr[3]}')