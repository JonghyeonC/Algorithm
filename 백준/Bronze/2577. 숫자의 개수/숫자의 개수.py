num = 1
num_list = [0] * 10
for _ in range(3):
    num *= int(input())

numbers = list(map(int, str(num)))
for i in numbers:
    num_list[i] += 1
for i in num_list:
    print(i)