N = int(input())
arr = list(map(int, input().split()))
ans = 0
for i in range(N):
    cnt = 0
    for j in range(i + 1, N):
        if arr[i] > arr[j]:
            cnt += 1
        else:
            if cnt > ans:
                ans = cnt
            break
    if cnt > ans:
        ans = cnt
print(ans)