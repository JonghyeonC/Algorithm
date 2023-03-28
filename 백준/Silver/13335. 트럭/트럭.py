import sys
from collections import deque


input = sys.stdin.readline

N, W, L = map(int, input().split())
trucks = deque(list(map(int, input().split())))
bridge = deque([0] * W)
time = 0

while bridge:
    bridge.popleft()
    time += 1
    if trucks:
        if sum(bridge) + trucks[0] <= L:
            temp = trucks.popleft()
            bridge.append(temp)
        else:
            bridge.append(0)

print(time)