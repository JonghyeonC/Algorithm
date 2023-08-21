import sys
input = sys.stdin.readline

N = int(input())
sec = list(map(int, input().split()))
yy = 0
mm = 0
for i in sec:
    yy += ((i // 30) + 1) * 10
    mm += ((i // 60) + 1) * 15
if mm < yy:
    print("M", mm)
elif yy < mm:
    print("Y", yy)
else:
    print("Y M", mm)