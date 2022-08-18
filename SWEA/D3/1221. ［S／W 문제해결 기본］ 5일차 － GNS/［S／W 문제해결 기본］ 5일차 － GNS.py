t = int(input())
for tc in range(1, t+1):

    a, b = map(str, input().split())
    b = int(b)
    text_list = list(map(str, input().split()))
    arr = [
        'ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN'
    ]
    ans_idx = [0] * 10
    answer = []
    #  arr의 단어와 입력받은 리스트의 값이 같을 경우 카운트를 하나씩 올리고, 그 값을 ans_idx에 순서대로 입력시킨다
    for i in range(10):
        cnt = 0
        for j in range(b):
            if text_list[j] == arr[i]:
                cnt += 1
        ans_idx[i] = cnt
    #  arr의 단어를 ans_idx의 해당하는 인덱스의 값만큼 answer리스트에 추가시킨다
    for i in range(10):
        for j in range(ans_idx[i]):
            answer.append(arr[i])

    print(f'#{tc}')
    for x in answer:
        print(x, end=' ')
    print()