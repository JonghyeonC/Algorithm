n = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]

width = 0
w_idx = 0
height = 0
h_idx = 0
for i in range(6):
    if arr[i][0] == 1 or arr[i][0] == 2:
        if width < arr[i][1]:
            width = arr[i][1]
            w_idx = i
    if arr[i][0] == 3 or arr[i][0] == 4:
        if height < arr[i][1]:
            height = arr[i][1]
            h_idx = i
big_rec = width * height

small_w = abs(arr[(h_idx + 1) % 6][1] - arr[(h_idx - 1) % 6][1])
small_h = abs(arr[(w_idx + 1) % 6][1] - arr[(w_idx - 1) % 6][1])
small_rec = small_h * small_w

rec = big_rec - small_rec

ans = rec * n
print(ans)