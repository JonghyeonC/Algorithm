def postorder(idx):
    if 1 <= idx <= N:
        if tree[idx] == '+':
            L = postorder(ch1[idx])
            R = postorder(ch2[idx])
            tree[idx] = L + R
        elif tree[idx] == '-':
            L = postorder(ch1[idx])
            R = postorder(ch2[idx])
            tree[idx] = L - R
        elif tree[idx] == '*':
            L = postorder(ch1[idx])
            R = postorder(ch2[idx])
            tree[idx] = L * R
        elif tree[idx] == '/':
            L = postorder(ch1[idx])
            R = postorder(ch2[idx])
            tree[idx] = L // R
        return tree[idx]


T = 10
for tc in range(1, T+1):
    N = int(input())
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    tree = [0] * (N + 1)
    for _ in range(N):
        node_list = list(input().split())
        idx = int(node_list[0])
        if node_list[1].isnumeric():
            tree[idx] = int(node_list[1])
        else:
            ch1[idx] = int(node_list[2])
            ch2[idx] = int(node_list[3])
            tree[idx] = node_list[1]

    ans = postorder(1)
    print(f'#{tc} {ans}')