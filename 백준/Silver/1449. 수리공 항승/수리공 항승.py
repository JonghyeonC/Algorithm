N, L = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

start = arr[0] - 0.5
tape = 1

for i in range(1, len(arr)):
    if start + L >= arr[i] + 0.5:
        continue
    else:
        start = arr[i] - 0.5
        tape += 1
print(tape)