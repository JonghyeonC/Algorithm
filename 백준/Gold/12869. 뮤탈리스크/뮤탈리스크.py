from itertools import permutations
from collections import deque
import copy


def bfs():
    q = deque()
    q.append((nums, 0))
    visited[nums[0]][nums[1]][nums[2]] = 1
    while q:
        num, cnt = q.popleft()
        if num == [0, 0, 0]:
            return cnt
        for attack in attack_possible:
            n_num = copy.deepcopy(num)
            if n_num[0] - attack[0] > 0:
                n_num[0] -= attack[0]
            else:
                n_num[0] = 0
            if n_num[1] - attack[1] > 0:
                n_num[1] -= attack[1]
            else:
                n_num[1] = 0
            if n_num[2] - attack[2] > 0:
                n_num[2] -= attack[2]
            else:
                n_num[2] = 0
            if visited[n_num[0]][n_num[1]][n_num[2]] == 0:
                q.append((n_num, cnt + 1))
                visited[n_num[0]][n_num[1]][n_num[2]] = 1


N = int(input())
nums = list(map(int, input().split()))
if len(nums) == 3:
    attacks = [9, 3, 1]
elif len(nums) == 2:
    attacks = [9, 3, 0]
    nums.append(0)
else:
    attacks = [9, 0, 0]
    nums.append(0)
    nums.append(0)

attack_possible = []
possibles = list(permutations(attacks, 3))
for possible in possibles:
    attack_possible.append(list(possible))
visited = [[[0 for _ in range(61)] for _ in range(61)] for _ in range(61)]
print(bfs())


