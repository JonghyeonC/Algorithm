def f(k, s):
    if sum(ans) > M:
        return
    if k == R:
        if sum(ans) == M:
            ans.sort()
            for i in ans:
                print(i)
            exit()
        else:
            return
    else:
        for i in range(s, N):
            ans.append(arr[i])
            f(k + 1, i + 1)
            ans.pop()


N = 9
R = 7
arr = [int(input()) for _ in range(9)]
M = 100
ans = []
f(0, 0)