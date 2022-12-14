N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

# 2차원 배열이지만 각각 세로줄 가로줄을 하나의 길로 보고 1차원씩 판단하여 문제를 해결한다.

# 가로 방향
for i in range(N):
    # 줄의 맨 처음 값을 기준으로 잡는다.
    height = arr[i][0]
    # 현재 위치에서 오른쪽으로 한 칸 이동 시킨다.
    j = 1
    # 이동되는 순간부터 길이를 1로 지정하기 위해서 1로 초기화를 한다.
    length = 1
    flag = 0
    while j < N:
        # 똑같은 값일 경우에
        if arr[i][j] == height:
            # 그 다음 위치로 넘어가는 경우에 길이를 가지고 넘어간다.
            length += 1
        # 값이 1 클 경우
        elif arr[i][j] == height + 1:
            # 길이가 경사로 길이보다 같거나 클 경우는 이동가능하다.
            if length >= L:
                # 기준 높이를 이동된 위치의 높이로 변경한다.
                height = arr[i][j]
                # 다시 길이를 1로 초기화한 상태로 다음 위치로 이동시킨다.
                length = 1
            else:
                flag = 1
                break
        # 값이 1 작을 경우
        elif arr[i][j] == height - 1:
            # 작아지는 경사로가 적합한지를 확인하기 위한 절차
            # 작아지는 값을 기준으로 잡는 새로운 높이를 만든다.
            n_height = arr[i][j]
            # 경사로의 길이를 구하기 위한 초기값
            n_length = 1
            # 경사로의 위치를 확인하기 위해서 오른쪽으로 이동시킨다.
            n_j = j + 1
            while n_j < N:
                if arr[i][n_j] == n_height:
                    n_length += 1
                    n_j += 1
                else:
                    break
            # 경사로의 길이가 충분하다면
            if n_length >= L:
                # 기준 높이를 낮아진 높이로 바꾼다.
                height = arr[i][j]
                # 이동시킬 가로 위치를 기준 길이보다 1작게 만들어 다음 반복문에서 위치가 1이 늘어났을 때 새로운 경사로 길이를 구할 때 추가되지 않도록 하기 위해서 0으로 초기화를 한다.
                length = 0
                # 만약 기준길이가 2인데 2만큼만 낮은 위치였다면 그 다음 반복문에서 위치를 1를 늘어났을 때 바로 높은 위치로 올라가므로 이것을 방지하기 위해서 기준 길이보다 1을 작게 만들어 다시 한번 체크시킨다.
                j = j + L - 1
            else:
                flag = 1
                break
        # 높이 차가 1보다 작거나 크거나 혹은 같은 경우를 제외한 모든 경우
        else:
            flag = 1
            break
        j += 1
    # flag가 0이라는 것은 문제가 없이 이동이 가능한 길이라는 뜻이므로 답으로 추가한다.
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
