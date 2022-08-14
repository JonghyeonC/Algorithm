t = int(input())
for tc in range(1, t+1):
    h_1, m_1, h_2, m_2 = map(int,input().split())
    h = 0
    m = 0

    if m_1 + m_2 >= 60:
        m = m_1 + m_2 - 60
        h = 1 + h_1 + h_2
    else:
        m = m_1 + m_2
        h = h_1 + h_2

    if h > 12:
        h -= 12

    print(f'#{tc} {h} {m}')