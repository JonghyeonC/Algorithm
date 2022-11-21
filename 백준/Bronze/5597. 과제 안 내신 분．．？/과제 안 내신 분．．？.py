arr = [num for num in range(1, 31)]
num_list = []
for _ in range(28):
    num = int(input())
    num_list.append(num)

not_in = []
for num in arr:
    if num not in num_list:
        not_in.append(num)
not_in.sort()
for num in not_in:
    print(num)