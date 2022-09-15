def inorder(idx):
    if idx:
        inorder(ch1[idx])
        ans.append(tree[idx])
        inorder(ch2[idx])


T = 10
for tc in range(1, T+1):
    N = int(input())
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    tree = [0] * (N + 1)
    for _ in range(N):
        num_list = input().split()
        idx = int(num_list[0])
        if len(num_list) == 4:
            tree[idx] = num_list[1]
            ch1[idx] = int(num_list[2])
            ch2[idx] = int(num_list[3])
        elif len(num_list) == 3:
            tree[idx] = num_list[1]
            ch1[idx] = int(num_list[2])
        elif len(num_list) == 2:
            tree[idx] = num_list[1]
    ans = []
    inorder(1)
    answer = ''.join(map(str, ans))
    print(f'#{tc} {answer}')