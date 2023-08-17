H, L = map(int, input().split())
N = int(input())
heights = [0, L]
widths = [0, H]
for _ in range(N):
    dir, leng = map(int, input().split())
    if dir == 0:
        heights.append(leng)
    elif dir == 1:
        widths.append(leng)

widths.sort()
heights.sort()

width_list = []
height_list = []

for i in range(len(widths) - 1):
    width_list.append(widths[i + 1] - widths[i])
for i in range(len(heights) - 1):
    height_list.append(heights[i + 1] - heights[i])
print(max(height_list) * max(width_list))
