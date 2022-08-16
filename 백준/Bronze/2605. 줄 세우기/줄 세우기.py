n = int(input())
arr = list(map(int, input().split()))
answer = []
for i in range(1, n+1):
    answer.insert(arr[i-1], i)
for i in answer[::-1]:
    print(i, end=' ')