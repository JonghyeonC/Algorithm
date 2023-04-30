import heapq, sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N = int(input())
    min_heap = []
    max_heap = []
    visited = [0] * 1000000
    for i in range(N):
        order, num = input().split()
        num = int(num)
        if order == "I":
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (num * -1, i))
            visited[i] = 1
        elif order == "D":
            if num == -1:
                while min_heap and visited[min_heap[0][1]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = 0
                    heapq.heappop(min_heap)
            elif num == 1:
                while max_heap and visited[max_heap[0][1]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = 0
                    heapq.heappop(max_heap)
    while min_heap and visited[min_heap[0][1]] == 0:
        heapq.heappop(min_heap)
    while max_heap and visited[max_heap[0][1]] == 0:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(max_heap[0][0] * -1, min_heap[0][0])
    else:
        print("EMPTY")
