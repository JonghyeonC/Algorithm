N = int(input())
arr = list(map(int, input().split()))
ans = 0
for num in arr:
    flag = 0
    for i in range(2, num):
        if num % i == 0:
            flag = 1
    if flag == 0 and num != 1:
        ans += 1
print(ans)