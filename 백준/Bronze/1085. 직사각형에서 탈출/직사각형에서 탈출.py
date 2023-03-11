x, y, w, h = map(int, input().split())
s_x, s_y = 0, 0
p1_x, p1_y = x - s_x, y - s_y
p2_x, p2_y = w - x, h -y
print(min(p1_x, p1_y, p2_x, p2_y))