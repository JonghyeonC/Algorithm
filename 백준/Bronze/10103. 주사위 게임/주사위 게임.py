scores = [100, 100]  # 창영, 상덕
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    if a > b:
        scores[1] -= a
    elif a < b:
        scores[0] -= b
    elif a == b:
        scores = scores
print(scores[0])
print(scores[1])