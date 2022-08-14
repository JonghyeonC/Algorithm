t = int(input())
for tc in range(1, t + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    total = 0
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    score_list = []
    rank_score = 0
    for i in range(n):
        total = arr[i][0] * 0.35 + arr[i][1] * 0.45 + arr[i][2] * 0.2
        score_list.append(total)

    rank_score = score_list[k-1]
    for i in range(n-1):
        max_idx = i
        for j in range(i+1, n):
            if score_list[j] > score_list[max_idx]:
                max_idx = j
        score_list[i], score_list[max_idx] = score_list[max_idx], score_list[i]

    rank_idx = 0
    a = 0
    for i in range(n):
        if rank_score == score_list[i]:
            rank_idx = i
            a = i // (n//10)
    print(f'#{tc} {grade[a]}')