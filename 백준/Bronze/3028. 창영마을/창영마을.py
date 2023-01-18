order = list(input())
arr = [1, 0, 0]
for alpha in order:
    if alpha == 'A':
        arr[0], arr[1] = arr[1], arr[0]
    elif alpha == 'B':
        arr[1], arr[2] = arr[2], arr[1]
    elif alpha == 'C':
        arr[0], arr[2]  = arr[2], arr[0]
for i in range(3):
    if arr[i] == 1:
        print(i + 1)