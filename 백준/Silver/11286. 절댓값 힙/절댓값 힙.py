import sys, heapq


input = sys.stdin.readline
N = int(input())
priority_queue = []
for _ in range(N):
    num = int(input())
    if num == 0:
        if len(priority_queue) == 0:
            print(0)
        else:
            print(heapq.heappop(priority_queue)[1])
    else:
        if num < 0:
            heapq.heappush(priority_queue, (num * -1, num))
        else:
            heapq.heappush(priority_queue, (num, num))