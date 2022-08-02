test_case = int(input())
num_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

for cnt in range(1, test_case + 1):
    num = int(input())
    num_str = str(num)
    num_list = []
    numbers = []
    num_sets = set()
    k = 1
    while True:
        numbers = list(str((k * num)))
        for i in numbers:
            num_list.append(i)
            num_sets = set(num_list)
        if num_sets != num_set:
            k += 1
        elif  num_sets == num_set:
            print(f'#{cnt} {k*num}')
            break