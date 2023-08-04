N = int(input())
for i in range(N):
    print('*' + '*' * i + ' ' * (N - 1 - i) + ' ' * (N - 1 - i) + '*' * i + '*')
for i in range(1, N):
    print('*' + '*' * (N - 1 - i) + ' ' * i + ' ' * i + '*' * (N - 1 - i) + '*')