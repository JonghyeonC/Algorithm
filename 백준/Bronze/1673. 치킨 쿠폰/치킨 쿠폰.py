while True:
    try:
        N, K = map(int, input().split())
        tmp = N
        ans = N
        while tmp >= K:
            ans += tmp // K
            tmp = tmp // K + tmp % K
        print(ans)
    except EOFError:
        break
