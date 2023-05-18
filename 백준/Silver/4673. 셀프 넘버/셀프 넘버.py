numbers = [0] * 10001
for num in range(1, 10001):
    tmp = num
    for i in str(num):
        tmp += int(i)
    if tmp < 10001:
        numbers[tmp] = 1
for i in range(1, 10001):
    if numbers[i] == 0:
        print(i)