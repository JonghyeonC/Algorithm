def dfs(v):
    visited[v] = 1              # 방문체크
    number = numbers[v-1]       # 배열에서 v에 해당하는 값이 다음 인덱스가 되지만 visited와 numbers의 인덱스가 같지 않으므로 -1
    if visited[number] == 0:    # 다음 인덱스가 방문한 적이 없다면 실행 아니면 종료
        dfs(number)


T = int(input())
for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    visited = [0] * (N+1)
    ans = 0

    for i in range(1, N+1):
        if visited[i] == 0:      # 아직 방문한 적이 없는 경우라면
            dfs(i)               # 사이클 확인
            ans += 1
    print(ans)