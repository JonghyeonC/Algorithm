arr = []
for _ in range(9):
    num = int(input())
    arr.append(num)
max_v = max(arr)
for i in range(9):
    if max_v == arr[i]:
        print(max_v)
        print(i + 1)