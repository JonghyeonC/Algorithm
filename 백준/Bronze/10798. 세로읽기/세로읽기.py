from collections import deque


aaa = deque(input())
bbb = deque(input())
ccc = deque(input())
ddd = deque(input())
eee = deque(input())

while True:
    if not aaa and not bbb and not ccc and not ddd and not eee:
        break
    if aaa:
        print(aaa.popleft(), end='')
    if bbb:
        print(bbb.popleft(), end='')
    if ccc:
        print(ccc.popleft(), end='')
    if ddd:
        print(ddd.popleft(), end='')
    if eee:
        print(eee.popleft(), end='')