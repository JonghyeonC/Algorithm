N = int(input())
name = [input() for _ in range(N)]
result = list(name[0])
for i in range(1, N):
    for j in range(len(result)):
        if result[j] != name[i][j]:
            result[j] = "?"
print("".join(result))