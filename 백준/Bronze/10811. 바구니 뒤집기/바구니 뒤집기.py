N, M = map(int, input().split(' '))
li = [n for n in range(1, N+1)]

for m in range(M):
    i, j = map(int, input().split(' '))
    li = li[:i-1] + li[i-1:j][::-1] + li[j:]

for rev in range(len(li)):
    print(li[rev], end=' ')