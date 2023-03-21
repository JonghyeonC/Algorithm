N = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
ans = 0
for i in range(N):
    temp = (i + 1) + arr[i]
    if temp > ans:
        ans = temp
print(ans + 1) # 이장님은 그 다음날 초대하니까 +1일