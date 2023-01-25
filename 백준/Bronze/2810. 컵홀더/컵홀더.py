N = int(input())
seat = input()
cnt = 0
for i in range(len(seat)):
    if seat[i] == 'L':
        cnt += 1

if cnt == 0:
    print(N)
else:
    print(N - ((cnt // 2) - 1))