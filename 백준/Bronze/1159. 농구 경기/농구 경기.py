import sys
input = sys.stdin.readline


N = int(input())
first = {}
for _ in range(N):
    word = input()
    if word[0] in first:
        first[word[0]] += 1
    else:
        first[word[0]] = 1
ans = []
for key, value in first.items():
    if value >= 5:
        ans.append(key)
if ans:
    ans.sort()
    print(''.join(ans))
else:
    print("PREDAJA")