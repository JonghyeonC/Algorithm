for _ in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

    ans = 'a'
    if x3 > x2 or y1 > y4 or x1 > x4 or y3 > y2:
        ans = 'd'
    if [x1, y1] == [x4, y4] or [x2, y1] == [x3, y4] or [x1, y2] == [x4, y3] or [x2, y2] == [x3, y3]:
        ans = 'c'

    if x4 == x1 and y4 > y1 and y2 > y3:
        ans = 'b'
    if y4 == y1 and x2 > x3 and x4 > x1:
        ans = 'b'
    if x3 == x2 and y4 > y1 and y2 > y3:
        ans = 'b'
    if y3 == y2 and x2 > x3 and x4 > x1:
        ans = 'b'
    print(ans)