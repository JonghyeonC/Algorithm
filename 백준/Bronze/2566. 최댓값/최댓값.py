arr = [list(map(int, input().split())) for _ in range(9)]
max_val = 0
idx_x = idx_y = 1
for i in range(9):
    for j in range(9):
        if arr[i][j] > max_val:
            max_val = arr[i][j]
            idx_x = i + 1
            idx_y = j + 1
print(max_val)
print(f'{idx_x} {idx_y}')