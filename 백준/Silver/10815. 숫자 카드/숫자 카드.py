N = int(input())
have = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))
have.sort()

ans = [0] * M


for i in range(M):
    s = 0
    e = N - 1
    while s <= e:
        mid = (s + e) // 2
        if check[i] == have[mid]:
            ans[i] += 1
            break
        elif check[i] > have[mid]:
            s = mid + 1
        elif check[i] < have[mid]:
            e = mid - 1
print(*ans)