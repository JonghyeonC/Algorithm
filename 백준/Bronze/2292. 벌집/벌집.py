N = int(input())
ans = 1
border = 1
time = 1
while True:
    if N <= border:
        break
    ans += 1
    border += 6 * time
    time += 1
print(ans)