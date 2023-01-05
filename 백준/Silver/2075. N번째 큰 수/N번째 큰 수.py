from queue import PriorityQueue
# 우선순위 큐를 사용 (넣을때는 상관없지만 알아서 오름차순으로 정렬
N = int(input())
q = PriorityQueue()

for _ in range(N):                      # 각 행마다 값 하나씩 비교
    arr = map(int, input().split())
    for num in arr:
        if len(q.queue) < N:            # 최대 나타낼 수 있는 길이보다 작다면
            q.put(num)                  # 계속 추가
        else:                           # 배열 갯수가 최대길이로만 유지할 수 있게 하기위해서
            if q.queue[0] < num:        # 젤 첨 비교값보다 크다면 기존 값은 빼고 새로운 값을 넣는다
                q.get()
                q.put(num)
print(q.queue[0])                       # 우선순위큐에서 가장 맨 앞의 값이 작은 것이므로 사용함.