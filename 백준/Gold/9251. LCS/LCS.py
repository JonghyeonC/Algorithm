import sys
input = sys.stdin.readline


word_1 = list(input().rstrip())
word_2 = list(input().rstrip())

dp = [[0] * (len(word_2) + 1) for _ in range(len(word_1) + 1)]
for i in range(1, len(word_1) + 1):
    for j in range(1, len(word_2) + 1):
        if word_1[i - 1] == word_2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[len(word_1)][len(word_2)])