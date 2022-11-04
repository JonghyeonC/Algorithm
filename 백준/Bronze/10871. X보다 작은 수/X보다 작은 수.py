N, M = map(int, input().split())
num_list = list(map(int, input().split()))

for num in num_list:
    if num < M:
        print(num, end=' ')