n = int(input())
total = 0
i = 1
while True:
    total += i
    if total <= n:
        i += 1
    else:
        print(i-1)
        break