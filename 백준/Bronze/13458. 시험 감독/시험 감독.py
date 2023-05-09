import sys
input = sys.stdin.readline


N = int(input())
tester = list(map(int, input().split()))
B, C = map(int, input().split())
ans = 0
for test in tester:
    tmp = test - B
    ans += 1
    if tmp > 0:
        if tmp % C:
            ans += (tmp // C) + 1
        elif tmp % C == 0:
            ans += tmp // C
print(ans)