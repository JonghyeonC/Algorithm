import sys
input = sys.stdin.readline


N = int(input())
num_list = list(map(int, input().split()))
sorted_num = sorted(num_list)

result = []
for i in range(N):
    for j in range(N):
        if num_list[i] == sorted_num[j]:
            result.append(j)
            sorted_num[j] = 0
            break

print(*result)