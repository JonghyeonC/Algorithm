n = int(input())
cups = [1, 2, 3]
for _ in range(n):
    a, b = map(int, input().split())
    index_i = cups.index(a)
    index_j = cups.index(b)
    cups[index_j], cups[index_i] = cups[index_i], cups[index_j]

print(cups[0])