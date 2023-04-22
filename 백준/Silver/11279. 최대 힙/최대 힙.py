import sys, heapq


input = sys.stdin.readline
N = int(input())
priority_queue = []
for _ in range(N):
    num = int(input())
    if num != 0:
        heapq.heappush(priority_queue, num * -1)
    else:
        if priority_queue:
            print(heapq.heappop(priority_queue) * -1)
        else:
            print(0)