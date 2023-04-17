import sys
from itertools import product


input = sys.stdin.readline
N, M = map(int, input().split())
num_list = [i for i in range(1, N + 1)]
result = list(product(num_list, repeat=M))   # 중복순열 구하는 함수 : product, 여기서 repeat를 통해서 "중복 가능한 n개 중에 r개를 나열하는 경우의 수"를 구할 수 있다
for ans in result:
    print(*ans)