t = int(input())
for tc in range(1, t+1):
    A, B = map(str, input().split())

    a = len(A)
    b = len(B)
    cnt = 0
    i = 0
    while len(A) >= len(B):
        if A[i: i + b] != B:
            i = 0
            A = A[i+1:]
        elif A[i: i + b] == B:
            cnt += 1
            A = A[i + b:]
            i = 0
    answer = a - b * cnt + cnt
    print(f'#{tc} {answer}')