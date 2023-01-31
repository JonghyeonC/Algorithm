N = int(input())
arr = list(map(int, input().split()))

arr.sort()
temp = [0] * N
temp[0] = arr[0]
for i in range(1, N):
    temp[i] = temp[i-1] + arr[i]

print(sum(temp))