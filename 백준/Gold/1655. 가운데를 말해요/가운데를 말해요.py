# 중간값을 기준으로 왼쪽(최대힙), 오른쪽(최소힙) 배열에 heapq로 넣으면서 
# 왼쪽 배열의 가장 큰 값(중간값보다는 작은)이 오른쪽 배열의 가장 작은 값(중간값보다는 큰) 크다면
# 서로 자리를 바꿔주면 중간값을 기준으로 오름차순 정렬을 할 수 있고, 왼쪽의 가장 큰 값을 출력하면 된다.
import heapq
import sys


input = sys.stdin.readline
N = int(input())
left = []
right = []
for _ in range(N):
    num = int(input())
    if len(left) == len(right):                     # 같은 크기라면 왼쪽부터 넣는다
        heapq.heappush(left, num * -1)              # 왼쪽은 pop하면 가장 큰 값을 출력시키기위해 최대힙으로 구현
    else:
        heapq.heappush(right, num)                  # 오른쪽은 pop하면 가장 작은 값 : 최소힙
    if left and right and left[0] * -1 > right[0]:  # 왼쪽의 가장 큰 값이 오른쪽의 가장 작은 값보다 크면 서로 자리를 바꾼다
        left_val = heapq.heappop(left)
        right_val = heapq.heappop(right)

        heapq.heappush(left, right_val * -1)
        heapq.heappush(right, left_val * -1)
    print(left[0] * -1)                             # 홀수라면 왼쪽부터 들어가므로 결국 왼쪽에서 가장 큰 값이 중간값이고,
                                                    # 짝수라도 왼쪽값이 더 작은 값이므로 왼쪽의 가장 큰 값을 출력하면 된다.