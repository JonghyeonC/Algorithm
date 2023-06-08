import sys
input = sys.stdin.readline().rstrip

a, b, x, c, d, y = map(int, input().split())
denom = a*d-b*c

ans_x = (d*x - b*y) // denom
ans_y = (-c*x + a*y) // denom

print(ans_x, ans_y)