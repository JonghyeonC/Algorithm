import sys
input = sys.stdin.readline

N = int(input().rstrip())
books = {}
for _ in range(N):
    title = input().rstrip()
    if title in books:
        books[title] += 1
    else:
        books[title] = 1

max_cnt = max(books.values())
result = []
for key, item in books.items():
    if item == max_cnt:
        result.append(key)
result.sort()
print(result[0])