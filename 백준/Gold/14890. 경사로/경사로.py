N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

# 가로 방향
for i in range(N):
    height = arr[i][0]
    j = 1
    length = 1
    flag = 0
    while j < N:
        # 똑같은 값일 경우에
        if arr[i][j] == height:
            length += 1
        # 값이 1 클 경우
        elif arr[i][j] == height + 1:
            if length >= L:
                height = arr[i][j]
                length = 1
            else:
                flag = 1
                break
        # 값이 1 작을 경우
        elif arr[i][j] == height - 1:
            n_height = arr[i][j]
            n_length = 1
            n_j = j + 1
            while n_j < N:
                if arr[i][n_j] == n_height:
                    n_length += 1
                    n_j += 1
                else:
                    break
            if n_length >= L:
                height = arr[i][j]
                length = 0
                j = j + L - 1
            else:
                flag = 1
                break
        else:
            flag = 1
            break
        j += 1
    if flag == 0:
        ans += 1

# 세로 방향
for j in range(N):
    height = arr[0][j]
    i = 1
    length = 1
    flag = 0
    while i < N:
        if arr[i][j] == height:
            length += 1
        elif arr[i][j] == height + 1:
            if length >= L:
                height = arr[i][j]
                length = 1
            else:
                flag = 1
                break
        elif arr[i][j] == height - 1:
            n_height = arr[i][j]
            n_length = 1
            n_i = i + 1
            while n_i < N:
                if arr[n_i][j] == n_height:
                    n_length += 1
                    n_i += 1
                else:
                    break
            if n_length >= L:
                height = n_height
                length = 0
                i = i + L - 1
            else:
                flag = 1
                break
        else:
            flag = 1
            break
        i += 1
    if flag == 0:
        ans += 1
print(ans)