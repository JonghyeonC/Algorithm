N = int(input())
arr = {}

for t in range(N):
    a, b = map(str,input().split())
    if b == 'enter':
        arr[a] = 'work'
    else:
        del arr[a]
arr = sorted(arr.keys(), reverse=True)
for i in arr:
    print(i)