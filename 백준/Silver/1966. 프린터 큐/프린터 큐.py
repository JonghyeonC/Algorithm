T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    idxs = list(range(len(arr)))
    idxs[M] = "check"

    ans = 0

    while True:
        if arr[0] == max(arr):
            ans += 1

            if idxs[0] == "check":
                print(ans)
                break
            else:
                arr.pop(0)
                idxs.pop(0)
        else:
            arr.append(arr.pop(0))
            idxs.append(idxs.pop(0))
