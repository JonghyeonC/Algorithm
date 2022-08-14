t = int(input())
for tc in range(1, t+1):
    m_1, d_1, m_2, d_2 = map(int, input().split())
    arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = 0

    if m_1 == m_2:
        answer = d_2 - d_1 + 1
    else:
        for i in range(m_1-1, m_2):
            answer += arr[i]
        answer = answer - d_1 - (arr[m_2-1] - d_2) + 1

    print(f'#{tc} {answer}')