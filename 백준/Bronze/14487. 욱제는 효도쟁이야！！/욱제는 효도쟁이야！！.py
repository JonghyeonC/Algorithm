N = int(input())
arr = list(map(int, input().split()))
max_v = max(arr)
print(sum(arr) - max_v)