num = int(input())
for tc in range(1, num+1):
    length = int(input())
    num_list = list(map(int, input()))
    cnt = 0
    answer = 0
    for i in range(length):
        if num_list[i] == 1:
            cnt += 1
            if answer < cnt:
                answer = cnt
        else:
            cnt = 0
    print(f'#{tc} {answer}')