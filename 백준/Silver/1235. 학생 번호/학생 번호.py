import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = []
for _ in range(N):
    arr.append((input().rstrip()))
k = 1
idx = len(arr[0])


while (idx - k) >= 0:
    tmp = []
    for i in range(N):
        tmp.append(arr[i][idx-k:idx])
    if len(set(tmp)) == N:
        break
    k += 1

print(k)