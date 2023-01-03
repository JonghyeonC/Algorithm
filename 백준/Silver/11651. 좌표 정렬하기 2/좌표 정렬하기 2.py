N = int(input())
num_list = []
for _ in range(N):
    num_list.append(list(map(int, input().split())))

answer = sorted(num_list, key=lambda x : (x[1], x[0]))
for ans in answer:
    print(*ans)