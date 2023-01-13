N, M, L = map(int, input().split())
seat = [0] * N
i = count = 0

while True:
    seat[i] += 1
    if seat[i] == M:
        break
    if seat[i] % 2 != 0:
        i = (i + L) % N
    else:
        i = (N + (i-L)) % N
    count += 1
print(count)