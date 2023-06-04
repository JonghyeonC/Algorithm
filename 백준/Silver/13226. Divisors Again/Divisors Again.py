import sys
from math import sqrt


input = sys.stdin.readline

N = int(input().rstrip())
for _ in range(N):
    a, b = map(int, input().rstrip().split())
    ans = 0
    for i in range(a, b + 1):
        tmp = 0
        for num in range(1, round(sqrt(i)) + 1):
            if i % num == 0 and num * num != i:
                tmp += 2
            if num * num == i:
                tmp += 1
        ans = max(ans, tmp)
    print(ans)