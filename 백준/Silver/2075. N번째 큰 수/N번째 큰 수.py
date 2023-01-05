from queue import PriorityQueue

N = int(input())
q = PriorityQueue()

for _ in range(N):
    arr = map(int, input().split())
    for num in arr:
        if len(q.queue) < N:
            q.put(num)
        else:
            if q.queue[0] < num:
                q.get()
                q.put(num)
print(q.queue[0])