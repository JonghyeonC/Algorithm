from itertools import permutations
from collections import deque
import copy


def bfs():
    q = deque()
    q.append((nums, 0))
    visited[nums[0]][nums[1]][nums[2]] = 1
    while q:
        num, cnt = q.popleft()
        if num == [0, 0, 0]:                                  # 다 죽었을 경우 cnt값을 리턴한다
            return cnt
        for attack in attack_possible:                        # 완전탐색으로 공격 가능한 모든 경우를 체크
            n_num = copy.deepcopy(num)                        # 기준 체력을 계속 복사하면서 각 공격에 대한 남은 체력을 체크하기 위함
            if n_num[0] - attack[0] > 0:
                n_num[0] -= attack[0]                         # 각 SCV를 공격할 때 체력이 0보다 크다면 데미지만큼 체력에서 뺌
            else:
                n_num[0] = 0                                  # 각 SCV를 공격할 때 체력이 0보다 작을 경우 0으로 만들기 위함
            if n_num[1] - attack[1] > 0:
                n_num[1] -= attack[1]
            else:
                n_num[1] = 0
            if n_num[2] - attack[2] > 0:
                n_num[2] -= attack[2]
            else:
                n_num[2] = 0
            if visited[n_num[0]][n_num[1]][n_num[2]] == 0:    # 각각의 체력이 중복되는 경우를 제하기 위함
                q.append((n_num, cnt + 1))                    # 각각의 체력이 중복되지 않으면 공격 횟수 증가
                visited[n_num[0]][n_num[1]][n_num[2]] = 1


N = int(input())
nums = list(map(int, input().split()))
if len(nums) == 3:                              # 입력받은 숫자가 3개일 때
    attacks = [9, 3, 1]                         # 순서에 따라 공격하는 데미지
elif len(nums) == 2:                            # 입력받은 숫자가 2개일 때
    attacks = [9, 3, 0]                         # 2개뿐이라면 마지막 공격은 생략
    nums.append(0)                              # 입력받은 숫자 리스트의 길이를 3으로 맞춘다
else:                                           # 입력받은 숫자가 1개일 때
    attacks = [9, 0, 0]                         # 1개뿐이라면 두번째, 마지막 공격은 생략
    nums.append(0)                              # 입력받은 숫자 리스트의 길이를 3으로 맞춘다
    nums.append(0)

attack_possible = []                            # 가능한 공격가능한 경우 리스트
possibles = list(permutations(attacks, 3))      # 순열 메서드를 사용해서 가능한 경우를 뽑는다
for possible in possibles:
    attack_possible.append(list(possible))      # 순열메서드를 사용하면 (?, ?, ?)라서 각 경우를 배열로 만들어주기 위해서
visited = [[[0 for _ in range(61)] for _ in range(61)] for _ in range(61)]  # 3차원 방문배열
print(bfs())
