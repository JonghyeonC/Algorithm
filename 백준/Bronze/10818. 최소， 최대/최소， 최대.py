N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
print(num_list[0], end=' ')
print(num_list[-1])