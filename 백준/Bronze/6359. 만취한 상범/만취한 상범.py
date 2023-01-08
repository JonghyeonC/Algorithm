T = int(input())
for _ in range(T):
    N = int(input())
    rooms = [True] * (N + 1) # True는 닫힌 상태
    for i in range(1, N + 1):
        for j in range(i, N + 1, i):
            if rooms[j]:
                rooms[j] = False
            else:
                rooms[j] = True
    print(rooms.count(False))