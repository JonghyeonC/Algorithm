N = int(input())
num_list = set()
for _ in range(N):
    num_list.add(int(input()))

num_list = list(num_list)
for num in sorted(num_list):
    print(num)