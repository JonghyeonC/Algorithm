N = int(input())
num_list = []
for _ in range(N):
    a, b = map(int, input().split())
    num_list.append((a, b))

for num in sorted(num_list):
    print(*num)