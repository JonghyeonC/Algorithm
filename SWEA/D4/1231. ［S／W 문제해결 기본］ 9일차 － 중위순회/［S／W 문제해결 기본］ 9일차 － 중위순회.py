def inorder(idx):
    if idx <= N:
        inorder(2 * idx)
        ans.append(tree[idx])
        inorder(2 * idx + 1)


T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N + 1)
    for _ in range(N):
        num_list = input().split()
        idx = int(num_list[0])
        tree[idx] = num_list[1]
    ans = []
    inorder(1)
    answer = ''.join(map(str, ans))
    print(f'#{tc} {answer}')