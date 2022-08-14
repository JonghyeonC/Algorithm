t = int(input())
for tc in range(1, t+1):
    sentence = input()
    pattern = ''
    l = 0
    '''
    pattern의 길이만큼의 구절을 찾게되면 pattern으로 인식하고 그 부분을 제거해서 남은 부분이 pattern의 길이보다 작다면
    pattern의 일부분이 아닌 걸로 간주한다
    '''
    for alpha in sentence:
        pattern += alpha
        l = len(pattern)
        if pattern == sentence[l:l*2]:
            last = sentence[l:]
            last = last.replace(pattern, '')
            if len(last) < l:
                break
    print(f'#{tc} {l}')