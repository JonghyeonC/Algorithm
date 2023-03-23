import heapq
import sys


input = sys.stdin.readline
N = int(input())
left = []
right = []
for _ in range(N):
    num = int(input())
    if len(left) == len(right):
        heapq.heappush(left, num * -1)
    else:
        heapq.heappush(right, num)
    if left and right and left[0] * -1 > right[0]:
        left_val = heapq.heappop(left)
        right_val = heapq.heappop(right)

        heapq.heappush(left, right_val * -1)
        heapq.heappush(right, left_val * -1)
    print(left[0] * -1)