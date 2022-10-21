N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1)
max_value = 0

#뒤에서부터 값을 비교해나가면서 최대값을 구한다.
for i in range(N-1, -1, -1):
    # 최대 비용을 구할려면 해당하는 위치의 값 + 그 값에 적힌 날짜이후의 값을 다 더하는 것이다
    t = arr[i][0] + i
    if t <= N:
        # 현재위치에서 지금까지의 합과 최대로 뒤로 갈 수 있는 날짜까지에서의 값의 합과 현재까지의 최대값을 비교
        dp[i] = max(arr[i][1] + dp[t], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value
        
print(max_value)