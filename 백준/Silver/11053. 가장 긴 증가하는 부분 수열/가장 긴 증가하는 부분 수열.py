N = int(input())
arr = list(map(int, input().split()))

result = [1] * N
for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            result[i] = max(result[i], result[j] + 1)
print(max(result))

# ans = 0
# for i in range(len(arr) - 1):
#     check = []
#     temp = arr[i]
#     check.append(temp)
#     for j in range(i, len(arr) - 1):
#         if temp < arr[j + 1]:
#             temp = arr[j + 1]
#             check.append(temp)
#         else:
#             temp = temp
#     ans = max(ans, len(check))
# print(ans)