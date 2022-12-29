s = input()
a = 'abcdefghijklmnopqrstuvwxyz'
arr = [-1] * 26

for i in s:
    arr[a.index(i)] = s.index(i)

print(*arr)