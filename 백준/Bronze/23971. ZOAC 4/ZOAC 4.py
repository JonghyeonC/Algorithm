import math

H, W, N, M = map(int, input().split())

sub_x = math.ceil(H/(N + 1))
sub_y = math.ceil(W/(M + 1))
print(sub_x * sub_y)