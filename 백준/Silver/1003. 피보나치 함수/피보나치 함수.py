import sys
input = sys.stdin.readline


def fibonacci(n):
    dp = [[1, 0], [0, 1]]
    for i in range(2, n + 1):
        dp.append([dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1]])
    return dp[n][0], dp[n][1]


T = int(input())
for _ in range(T):
    N = int(input())
    a, b = fibonacci(N)
    print(a, b)