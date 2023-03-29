import sys, heapq


input = sys.stdin.readline
N = int(input())
arr = []
dasom = int(input())
for _ in range(N - 1):
    heapq.heappush(arr, -int(input()))

cnt = 0

if arr:
    while True:
        if dasom > -arr[0]:
            break
        else:
            dasom += 1
            temp = -(heapq.heappop(arr))
            temp -= 1
            heapq.heappush(arr, -temp)
        cnt += 1

print(cnt)