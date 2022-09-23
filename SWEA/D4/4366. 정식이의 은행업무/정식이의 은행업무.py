def bi_num(num):
    n = len(num)
    total = 0
    for i in range(n - 1, -1, -1):
        total += 2 ** (n - 1 - i) * int(num[i])
    return total


def tri_num(num):
    n = len(num)
    total = 0
    for i in range(n - 1, -1, -1):
        total += 3 ** (n - 1 - i) * int(num[i])
    return total


T = int(input())
for tc in range(1, T + 1):
    bi_text = list(input())
    tri_text = list(input())
    check_2 = []
    check_3 = []
    for i in range(len(bi_text)):
        if bi_text[i] == '0':
            bi_text[i] = '1'
            check_2.append(''.join(bi_text))
            bi_text[i] = '0'
        elif bi_text[i] == '1':
            bi_text[i] = '0'
            check_2.append(''.join(bi_text))
            bi_text[i] = '1'

    for i in range(len(tri_text)):
        if tri_text[i] == '0':
            tri_text[i] = '1'
            check_3.append(''.join(tri_text))
            tri_text[i] = '0'
            tri_text[i] = '2'
            check_3.append(''.join(tri_text))
            tri_text[i] = '0'
        elif tri_text[i] == '1':
            tri_text[i] = '0'
            check_3.append(''.join(tri_text))
            tri_text[i] = '1'
            tri_text[i] = '2'
            check_3.append(''.join(tri_text))
            tri_text[i] = '1'
        elif tri_text[i] == '2':
            tri_text[i] = '0'
            check_3.append(''.join(tri_text))
            tri_text[i] = '2'
            tri_text[i] = '1'
            check_3.append(''.join(tri_text))
            tri_text[i] = '2'
    for i in range(len(check_2)):
        for j in range(len(check_3)):
            if bi_num(check_2[i]) == tri_num(check_3[j]):
                ans = bi_num(check_2[i])
    print(f'#{tc} {ans}')