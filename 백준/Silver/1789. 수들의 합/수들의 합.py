import sys
a = int(sys.stdin.readline())
cnt = 1
ans = 0
while True:
    if a < cnt:
       break
    else:
        a = a - cnt
        cnt += 1
        ans += 1
print(ans)