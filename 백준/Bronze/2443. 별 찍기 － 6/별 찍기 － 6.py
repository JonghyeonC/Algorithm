N = int(input())
for i in range(N):
    print(' ' * i + '*' * (N - i - 1) + '*' + '*' * (N - i - 1))